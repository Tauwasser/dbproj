# Generated by Django 2.2.1 on 2019-05-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcbs', '0021_create_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
    ]