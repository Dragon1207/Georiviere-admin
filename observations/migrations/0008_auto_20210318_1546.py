# Generated by Django 3.1.6 on 2021-03-18 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0007_remove_station_station_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='station_profile',
            new_name='station_profiles',
        ),
    ]
