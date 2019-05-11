# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Manufacturer, System, PCB, PCBRevision


def getSidebarData():
    # transform PCBs into dict of {systems: {manufacturer: [pcb]}}
    systems = System.objects.all()
    manufacturers = Manufacturer.objects.all()
    pcbs = PCB.objects.all()
    sidebar = {
        system: {
            manufacturer: pcbs.filter(manufacturer=manufacturer, system=system)
            for manufacturer in manufacturers.order_by('name')
        } for system in systems.order_by('name')
    }
    return sidebar


def index(request, system_slug=None):
    sidebar = getSidebarData()
    if (system_slug is not None):
        system = get_object_or_404(System, slug__iexact=system_slug)
    elif (system_slug is None):
        system = System.objects.first()
    defManufacturer = Manufacturer.objects.first()
    return render(request,
                  'pcbs/index.html',
                  {
                      'sidebar': sidebar,
                      'pcb': PCB(name='Bogus', system=system, manufacturer=defManufacturer)
                  }
                  )


def details(request, system_slug, pcb_slug):

    system = get_object_or_404(System, slug__iexact=system_slug)

    pcb_parts = pcb_slug.rsplit('-', 1)
    pcb_name = pcb_parts[0]
    pcb_revision = pcb_parts[-1]

    try:
        pcb_revision = PCBRevision.objects.get(
                                               label__iexact=pcb_revision,
                                               pcb__name__iexact=pcb_name,
                                               pcb__system=system
                                               )
        pcb = pcb_revision.pcb
    except PCBRevision.DoesNotExist:
        pcb = get_object_or_404(PCB, name__iexact=pcb_slug, system=system)

    sidebar = getSidebarData()
    return render(request,
                  'pcbs/details.html',
                  {
                      'sidebar': sidebar,
                      'pcb': pcb
                  }
                  )
