from django.db import models


class Manufacturer(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'System'
        verbose_name_plural = 'Systems'

    def __str__(self):
        return self.name


class PCB(models.Model):
    name = models.CharField(max_length=32)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'PCB'
        verbose_name_plural = 'PCBs'

    def __str__(self):
        return self.name


class PCBRevision(models.Model):
    pcb = models.ForeignKey(PCB, on_delete=models.PROTECT)
    label = models.CharField(max_length=16, blank=True)
    changes = models.TextField(blank=True)
    is_base_revision = models.BooleanField(default=False, verbose_name='Base Revision')

    class Meta:
        verbose_name = 'PCB Revision'
        verbose_name_plural = 'PCB Revisions'
        unique_together = (('pcb', 'label'),)

    def __str__(self):
        if ('' != self.label):
            return self.pcb.name + '-' + self.label
        return self.pcb.name
