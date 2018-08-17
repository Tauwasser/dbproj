# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from .models import Game, GameTitle, Language


class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):

        if isinstance(o, Game) or isinstance(o, GameTitle) or isinstance(o, Language):
            return model_to_dict(o)

        return super().default(o)


def index(request):
    return render(request, 'dumps/index.html', {})


def find_games(request):
    searchTerm = request.GET.get('searchTerm', None)
    games = Game.objects.filter(gametitle__title__icontains=searchTerm).distinct()

    gamesFound = [
        {
            'id': x.id,
            'name': str(x),
            'codes': list(set(filter(None, x.gametitle_set.values_list('code', flat=True))))
        } for x in games]

    data = {
        'games_found': gamesFound,
    }
    return JsonResponse(data, encoder=ExtendedEncoder)
