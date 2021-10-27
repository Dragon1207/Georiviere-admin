# Generated by Django 3.1.6 on 2021-03-22 15:22

from django.db import migrations, models
import django.db.models.deletion
import geotrek.authent.models


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0005_remove_userprofile_language'),
        ('observations', '0009_auto_20210318_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='structure',
            field=models.ForeignKey(default=geotrek.authent.models.default_structure_pk, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure'),
        ),
        migrations.AddField(
            model_name='stationprofile',
            name='structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.structure', verbose_name='Related structure'),
        ),
    ]
