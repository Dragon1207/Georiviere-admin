# Generated by Django 3.1.6 on 2021-04-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0008_auto_20210413_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topology',
            name='stream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topologies', to='river.stream', verbose_name='Stream'),
        ),
    ]
