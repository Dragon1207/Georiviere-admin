# Generated by Django 3.1.5 on 2021-01-25 17:25

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0002_auto_20210201_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='geom',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=settings.SRID),
        ),
    ]
