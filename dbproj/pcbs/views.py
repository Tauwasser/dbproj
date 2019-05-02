# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Manufacturer, System, PCB


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


def index(request, system=None):
    sidebar = getSidebarData()
    if (system is not None):
        system = get_object_or_404(System, name__iexact=system)
    if (system is None):
        system = System.objects.first()
    defManufacturer = Manufacturer.objects.first()
    return render(request,
                  'pcbs/index.html',
                  {
                      'sidebar': sidebar,
                      'pcb': PCB(name='Bogus', system=system, manufacturer=defManufacturer)
                  }
                  )


def details(request, system, pcb):

    system = get_object_or_404(System, name__iexact=system)

    pcb_name = pcb if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[0]
    pcb_revision = None if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[1]

    pcb = get_object_or_404(PCB, name__iexact=pcb_name, system=system)

    sidebar = getSidebarData()
    return render(request,
                  'pcbs/details.html',
                  {
                      'sidebar': sidebar,
                      'pcb': pcb
                  }
                  )
