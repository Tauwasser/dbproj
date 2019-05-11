from django.contrib import admin

from .models import *


class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer',)
    prepopulated_fields = {"slug": ("name",)}


class PCBRevisionInline(admin.StackedInline):
    model = PCBRevision
    extra = 0


class PCBAdmin(admin.ModelAdmin):
    list_display = ('name', 'system', 'manufacturer',)

    fieldsets = [
        (None, {'fields': ['name', 'system', 'manufacturer']}),
    ]
    inlines = [PCBRevisionInline]


admin.site.register(Manufacturer)
admin.site.register(System, SystemAdmin)
admin.site.register(PCB, PCBAdmin)

