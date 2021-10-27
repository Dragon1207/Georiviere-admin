# Generated by Django 3.1.6 on 2021-10-12 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0008_auto_20210915_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='bank_effect',
        ),
        migrations.RemoveField(
            model_name='work',
            name='code_stake',
        ),
        migrations.RemoveField(
            model_name='work',
            name='mobility',
        ),
        migrations.RemoveField(
            model_name='work',
            name='pit_height',
        ),
        migrations.AddField(
            model_name='work',
            name='downstream_bank_effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='downstream_works', to='knowledge.workbankeffect', verbose_name='Bank effect'),
        ),
        migrations.AddField(
            model_name='work',
            name='upstream_bank_effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upstream_works', to='knowledge.workbankeffect', verbose_name='Upstream bank effect'),
        ),
    ]
