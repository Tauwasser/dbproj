# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class System(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=16)

    def __str__(self):
        return self.name

#class Game(models.Model):
#    system = models.ForeignKey(System,on_delete=models.PROTECT,db_index=false)
#    name = models.CharField(max_length=128)
#    region
#    date_published
#    sha256sum
#    sha1sum
#    md5sum
#
#class Dump(models.Model):
#    system = models.ForeignKey(System)
#    date
    
