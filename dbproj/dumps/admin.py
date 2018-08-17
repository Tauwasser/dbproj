# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import System, Game, Language, GameTitle


class GameTitleInline(admin.TabularInline):
    model = GameTitle
    extra = 1


class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['system', 'langs']}),
    ]
    inlines = [GameTitleInline]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Game, GameAdmin)
admin.site.register(Language)
admin.site.register(System)

