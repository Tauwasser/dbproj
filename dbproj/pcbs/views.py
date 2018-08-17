# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import System, PCB

# Create your views here.

def index(request):
    systems = System.objects.order_by('name')
    return render(request, 'pcbs/index.html', {'systems': systems})

def details(request, system, pcb):
    systems = System.objects
    sel_system = System.objects.get(name__iexact=system)
    pcb_name = pcb if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[0]
    pcb_revision = None if pcb.count('-') <= 1 else pcb.rsplit('-', 1)[1]
    sel_pcb = None
    pcb_candidates = PCB.objects.filter(name__iexact=pcb_name, group__system=sel_system)
    return render(request, 'pcbs/details.html', {'systems': systems, 'sel_system': sel_system, 'pcb_candidates': pcb_candidates})
