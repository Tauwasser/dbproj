# Generated by Django 2.2.1 on 2019-05-02 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0014_auto_20190502_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcbgroup',
            name='manufacturer_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pcbs.Manufacturer'),
        ),
    ]
