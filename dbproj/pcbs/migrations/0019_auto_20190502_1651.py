# Generated by Django 2.2.1 on 2019-05-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0018_move_pcbGroup_details_to_PCB'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcb',
            name='group',
        ),
        migrations.DeleteModel(
            name='PCBGroup',
        ),
    ]