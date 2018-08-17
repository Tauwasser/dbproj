# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, GameTitle, Language


def index(request):
    return render(request, 'dumps/index.html', {})

