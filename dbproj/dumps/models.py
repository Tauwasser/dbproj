# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=64)
    localName = models.CharField(max_length=64)
    ietfTag = models.CharField(max_length=16, verbose_name='IETF Language Tag')
    isDisplayLanguage = models.BooleanField()
    isLatinScript = models.BooleanField()

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Game(models.Model):
    system = models.ForeignKey(System, on_delete=models.PROTECT, db_index=False)
    langs = models.ManyToManyField(Language,
                                   limit_choices_to={'isDisplayLanguage': True},
                                   verbose_name='Text Languages'
                                   )

    def __str__(self):
        firstTitle = self.gametitle_set.all().first()
        title = firstTitle.title if firstTitle is not None else '<Untitled>'
        langs = self.langs.all()
        langMarker = ''
        if (1 < len(langs)):
            langMarker = '(' + ','.join(sorted([x.ietfTag.title() for x in langs])) + ')'
        region = ''
        nameComponents = [title, langMarker, region]
        return ' '.join([x for x in nameComponents if x])


class GameTitle(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT, db_index=True)
    title = models.CharField(max_length=128)
    lang = models.ForeignKey(Language, on_delete=models.PROTECT, verbose_name='Language')
    code = models.CharField(max_length=32, verbose_name='Game Code', blank=True)

    def __str__(self):
        return self.title

# class Game(models.Model):
#     system = models.ForeignKey(System,on_delete=models.PROTECT,db_index=false)
#     name = models.CharField(max_length=128)
#     region
#     date_published
#     sha256sum
#     sha1sm
#     md5sum
#
# class Dump(models.Model):
#     system = models.ForeignKey(System)
#     date
