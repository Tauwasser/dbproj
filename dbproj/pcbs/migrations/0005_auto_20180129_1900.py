# Generated by Django 2.0.1 on 2018-01-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0004_auto_20180129_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcbrevision',
            name='differences',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pcbrevision',
            name='label',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
