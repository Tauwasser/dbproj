# Generated by Django 2.1 on 2018-08-16 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dumps', '0002_auto_20180816_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gametitle',
            name='langs',
        ),
        migrations.AddField(
            model_name='gametitle',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dumps.Language'),
            preserve_default=False,
        ),
    ]
