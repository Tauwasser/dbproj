# Generated by Django 2.0.1 on 2018-01-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0006_auto_20180129_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcbrevision',
            name='is_base_revision',
            field=models.BooleanField(default=False, verbose_name='Base Revision'),
        ),
    ]
