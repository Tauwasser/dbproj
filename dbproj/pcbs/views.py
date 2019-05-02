# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Manufacturer, System, PCB


def index(request):
    systems = System.objects.order_by('name')
    return render(request, 'pcbs/index.html', {'systems': systems})


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


def details(request, system, pcb):
    system = System.objects.get(name__iexact=system)

    if (system is None):
        # TODO: re-route to index
        pass

    pcb_name = pcb if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[0]
    pcb_revision = None if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[1]

    pcb = PCB.objects.get(name__iexact=pcb_name, system=system)
    if (pcb is None):
        # TODO: re-route to system
        pass

    sidebar = getSidebarData()
    return render(request,
                  'pcbs/details.html',
                  {
                      'sidebar': sidebar,
                      'pcb': pcb
                  }
                  )
