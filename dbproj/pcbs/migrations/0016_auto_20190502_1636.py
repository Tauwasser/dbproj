# Generated by Django 2.2.1 on 2019-05-02 16:36

from django.db import migrations


def create_PCB_Manufacturers(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    PCBGroup = apps.get_model("pcbs", "PCBGroup")
    Manufacturer = apps.get_model("pcbs", "Manufacturer")
    for pcbGrp in PCBGroup.objects.all():
        manufacturer, created = Manufacturer.objects.get_or_create(name=pcbGrp.name)
        pcbGrp.manufacturer_fk = manufacturer
        pcbGrp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0015_pcbgroup_manufacturer_fk'),
    ]

    operations = [
        migrations.RunPython(create_PCB_Manufacturers),
    ]