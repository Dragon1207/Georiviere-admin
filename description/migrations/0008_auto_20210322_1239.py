# Generated by Django 3.1.7 on 2021-03-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('description', '0007_auto_20210302_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='agreement',
            field=models.BooleanField(default=False, verbose_name='Agreement'),
        ),
        migrations.AddField(
            model_name='land',
            name='identifier',
            field=models.CharField(blank=True, max_length=255, verbose_name='Identifier'),
        ),
    ]
