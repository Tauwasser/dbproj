# Generated by Django 2.0.1 on 2018-01-29 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0002_pcb_revision'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pcb',
            options={'verbose_name': 'PCB', 'verbose_name_plural': 'PCBs'},
        ),
        migrations.AlterModelOptions(
            name='revision',
            options={'verbose_name': 'Revision', 'verbose_name_plural': 'Revisions'},
        ),
        migrations.AlterModelOptions(
            name='system',
            options={'verbose_name': 'System', 'verbose_name_plural': 'Systems'},
        ),
    ]
