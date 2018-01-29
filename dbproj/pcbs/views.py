# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import System

# Create your views here.

def index(request):
    systems = System.objects.order_by('name')
    html = '<br />'.join([s.name for s in systems])
    return HttpResponse(html)
