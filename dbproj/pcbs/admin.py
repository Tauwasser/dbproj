from django.contrib import admin

from .models import *


class PCBRevisionInline(admin.StackedInline):
    model = PCBRevision
    extra = 0


class PCBAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'group']}),
    ]
    inlines = [PCBRevisionInline]


admin.site.register(Manufacturer)
admin.site.register(System)
admin.site.register(PCB, PCBAdmin)
admin.site.register(PCBGroup)

