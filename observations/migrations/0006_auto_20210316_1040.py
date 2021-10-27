# Generated by Django 3.1.6 on 2021-03-16 10:23

from django.db import migrations


def station_type_to_profile(apps, schema_editor):
    Station = apps.get_model('observations', 'Station')
    StationProfile = apps.get_model('observations', 'StationProfile')

    for station in Station.objects.all():
        station_profile, created = StationProfile.objects.get_or_create(
            code=station.station_type,
            defaults={
                'label': station.get_station_type_display(),
            }
        )
        station.station_profile.add(station_profile)


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0005_auto_20210316_1038'),
    ]

    operations = [
        migrations.RunPython(station_type_to_profile),
    ]
