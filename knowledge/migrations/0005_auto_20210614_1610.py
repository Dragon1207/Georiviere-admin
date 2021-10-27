# Generated by Django 3.1.6 on 2021-06-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0004_auto_20210531_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetationSpecificDiversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Specific diversity',
                'verbose_name_plural': 'Specific diversities',
            },
        ),
        migrations.RenameModel(
            old_name='VegetationClass',
            new_name='VegetationAgeClassDiversity',
        ),
        migrations.AlterModelOptions(
            name='vegetationageclassdiversity',
            options={'verbose_name': 'Age class diversity', 'verbose_name_plural': 'Age class diversities'},
        ),
        migrations.AlterModelOptions(
            name='worksedimenteffect',
            options={'verbose_name': 'Work sediment effect', 'verbose_name_plural': 'Work sediment effects'},
        ),
        migrations.RenameField(
            model_name='vegetation',
            old_name='vegetation_class',
            new_name='age_class_diversity',
        ),
        migrations.RenameField(
            model_name='vegetation',
            old_name='stratum',
            new_name='strata',
        ),
        migrations.RemoveField(
            model_name='vegetation',
            name='label',
        ),
        migrations.RemoveField(
            model_name='vegetation',
            name='specific_variety',
        ),
        migrations.RemoveField(
            model_name='work',
            name='label',
        ),
        migrations.AlterField(
            model_name='vegetation',
            name='knowledge',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='knowledge.knowledge', verbose_name='Knowledge'),
        ),
        migrations.AlterField(
            model_name='work',
            name='knowledge',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='knowledge.knowledge', verbose_name='Knowledge'),
        ),
        migrations.AddField(
            model_name='vegetation',
            name='specific_diversity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='knowledge.vegetationspecificdiversity', verbose_name='Specific variety'),
            preserve_default=False,
        ),
    ]
