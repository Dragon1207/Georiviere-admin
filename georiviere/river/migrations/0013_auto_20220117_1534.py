# Generated by Django 3.1.13 on 2022-01-17 15:34

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0012_add_source_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='source_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=2154, verbose_name='Source location'),
        ),
    ]