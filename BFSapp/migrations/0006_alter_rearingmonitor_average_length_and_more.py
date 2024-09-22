# Generated by Django 5.1.1 on 2024-09-22 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BFSapp', '0005_alter_breedmonitor_amount_of_eggs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rearingmonitor',
            name='average_length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='box',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='cage_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='consortium_entoprotech_breeding',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='cooking_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='crate_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='cycle',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='days_from_cooking',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='days_from_laying',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='diet_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='eggs_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BFSapp.eggmonitor'),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='goal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='harvest_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='larvae_pupae_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='length_measure_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='measure_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='number_of_larvae_pupae_sampled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='number_of_larvae_sampled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='pupation_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='single_larva_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='single_larvae_pupae_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='starter_age',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='starter_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='starter_diet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='starter_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='substrate_after_drying',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='substrate_before_drying',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='survival_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='total_larvae_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='total_larvae_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rearingmonitor',
            name='total_pupae_larvae_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
