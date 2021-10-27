# Generated by Django 3.1.6 on 2021-10-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances_administration', '0005_auto_20211020_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeoperation',
            name='manday_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Subcontract cost'),
        ),
    ]
