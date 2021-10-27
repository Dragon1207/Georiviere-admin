# Generated by Django 3.1.6 on 2021-03-24 10:23

import colorfield.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatershedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('color', colorfield.fields.ColorField(default='#444444', help_text='Color shown on map', max_length=18, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Watershed type',
            },
        ),
        migrations.CreateModel(
            name='Watershed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2154)),
                ('eid', models.CharField(blank=True, default=None, max_length=1024, null=True, unique=True, verbose_name='External id')),
                ('watershed_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='watershed.watershedtype', verbose_name='Watershed')),
            ],
            options={
                'verbose_name': 'Watershed',
                'verbose_name_plural': 'Watersheds',
                'ordering': ['watershed_type', 'name'],
            },
        ),
    ]
