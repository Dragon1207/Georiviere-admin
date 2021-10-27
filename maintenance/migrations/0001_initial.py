# Generated by Django 3.1.6 on 2021-08-02 09:09

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import geotrek.authent.models
import geotrek.zoning.mixins
import watershed.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authent', '0005_remove_userprofile_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterventionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Type')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure')),
            ],
            options={
                'verbose_name': "Intervention's type",
                'verbose_name_plural': "Intervention's types",
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='InterventionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Status')),
                ('order', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Display order')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure')),
            ],
            options={
                'verbose_name': "Intervention's status",
                'verbose_name_plural': "Intervention's statuses",
                'ordering': ['order', 'label'],
            },
        ),
        migrations.CreateModel(
            name='InterventionStake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Type')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure')),
            ],
            options={
                'verbose_name': "Intervention's stake",
                'verbose_name_plural': "Intervention's stakes",
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='InterventionDisorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Disorder')),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure')),
            ],
            options={
                'verbose_name': "Intervention's disorder",
                'verbose_name_plural': "Intervention's disorders",
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_insert', models.DateTimeField(auto_now_add=True, verbose_name='Insertion date')),
                ('date_update', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Update date')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Date')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=2154)),
                ('description', models.TextField(blank=True, help_text='Remarks and notes', verbose_name='Description')),
                ('width', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Width')),
                ('height', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Height')),
                ('area', models.FloatField(blank=True, default=0, editable=False, null=True, verbose_name='Area')),
                ('disorders', models.ManyToManyField(blank=True, related_name='interventions', to='maintenance.InterventionDisorder', verbose_name='Disorders')),
                ('intervention_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.interventionstatus', verbose_name='Status')),
                ('intervention_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.interventiontype', verbose_name='Type')),
                ('stake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interventions', to='maintenance.interventionstake', verbose_name='Stake')),
                ('structure', models.ForeignKey(default=geotrek.authent.models.default_structure_pk, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure')),
            ],
            options={
                'verbose_name': 'Intervention',
                'verbose_name_plural': 'Interventions',
            },
            bases=(watershed.mixins.WatershedPropertiesMixin, geotrek.zoning.mixins.ZoningPropertiesMixin, models.Model),
        ),
    ]
