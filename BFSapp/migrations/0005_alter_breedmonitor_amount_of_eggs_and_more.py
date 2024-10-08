# Generated by Django 5.1 on 2024-08-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BFSapp', '0004_alter_breedmonitor_days_from_cage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedmonitor',
            name='amount_of_eggs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='avg_fertility',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='avg_oviposition',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='cage_geometry',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='days_for_first_egg_from_emer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='days_from_egg_placement',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='from_hatch_to_emer_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='mg_eggs_female',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='num_clutches',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='num_eggs_female',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='num_females',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='oviposition',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='peak_daily',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='pupae',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='single_larvae',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='target_density',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedmonitor',
            name='total_eggs_harvest',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
