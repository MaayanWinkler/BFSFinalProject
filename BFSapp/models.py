from django.db import models
# from .managers import MeasurementManager

# Create your models here.
# class Measurement(models.Model):
#     cycle = models.IntegerField()
#     diet = models.CharField(max_length=1)
#     date = models.DateField()

#     temperature = models.FloatField()
#     larvae_weight = models.FloatField()
#     before_dry = models.FloatField()
#     after_dry = models.FloatField()
    
#     # objects = MeasurementManager()
    
#     def __str__(self):
#         return f'Measurement - {self.cycle}, {self.diet}, {self.date}'

class EggMonitor(models.Model):
    date_measure = models.DateTimeField()
    passed_hours = models.FloatField()
    cage_code = models.CharField(max_length=100)
    eggs_code = models.CharField(max_length=100)
    
    egg_weight_1 = models.FloatField(null=True, blank=True)
    egg_weight_2 = models.FloatField(null=True, blank=True)
    egg_weight_3 = models.FloatField(null=True, blank=True)
    
    num_eggs_1 = models.IntegerField(null=True, blank=True)
    num_eggs_2 = models.IntegerField(null=True, blank=True)
    num_eggs_3 = models.IntegerField(null=True, blank=True)
    
    avg_single_weight = models.FloatField(null=True, blank=True)
    rsd_single_weight = models.FloatField(null=True, blank=True)
    total_eggs_weight = models.IntegerField(null=True, blank=True)
    added_eggs = models.FloatField(null=True, blank=True)
    
    fertile_eggs_1 = models.IntegerField(null=True, blank=True)
    fertile_eggs_2 = models.IntegerField(null=True, blank=True)
    fertile_eggs_3 = models.IntegerField(null=True, blank=True)
    
    infertile_eggs_1 = models.IntegerField(null=True, blank=True)
    infertile_eggs_2 = models.IntegerField(null=True, blank=True)
    infertile_eggs_3 = models.IntegerField(null=True, blank=True)
    
    fertelity_percentage = models.FloatField(null=True, blank=True)
    rsd_fertelity_percentage = models.FloatField(null=True, blank=True)
    
    target_density = models.IntegerField(null=True, blank=True)
    amount_of_added_eggs = models.FloatField(null=True, blank=True)
    
    incubation_temp = models.CharField(max_length=50, null=True, blank=True)
    incubation_tube = models.CharField(max_length=50, null=True, blank=True)
    
    comments = models.CharField(max_length=50, null=True, blank=True)

class RearingMonitor(models.Model):
    crate_code = models.CharField(max_length = 100)
    consortium_entoprotech_breeding = models.CharField(max_length=100)
    cycle = models.IntegerField()
    box = models.IntegerField()
    goal = models.CharField(max_length=100)
    eggs_code = models.ForeignKey(EggMonitor, on_delete=models.CASCADE)
    starter_date = models.DateTimeField()
    starter_size = models.IntegerField()
    starter_diet = models.CharField(max_length=100)
    length_measure_date = models.DateTimeField()
    average_length = models.FloatField()
    starter_age = models.FloatField()
    cooking_date = models.DateTimeField()
    diet_type = models.CharField(max_length=100)
    measure_date = models.DateTimeField()
    temperature = models.FloatField()
    total_larvae_weight = models.IntegerField()
    number_of_larvae_sampled = models.IntegerField()
    single_larva_weight = models.IntegerField()
    pupation_percentage = models.FloatField()
    substrate_before_drying = models.FloatField()
    substrate_after_drying = models.FloatField()
    harvest_date = models.DateTimeField()
    days_from_laying = models.IntegerField()
    days_from_cooking = models.IntegerField()
    total_pupae_larvae_weight = models.FloatField()
    larvae_pupae_weight = models.FloatField()
    number_of_larvae_pupae_sampled = models.IntegerField()
    single_larvae_pupae_weight = models.IntegerField()
    total_larvae_count = models.IntegerField()
    survival_percentage = models.IntegerField()
    cage_code = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

class BreedMonitor(models.Model):
    crate_code = models.ForeignKey(RearingMonitor, on_delete=models.CASCADE, related_name='breedmonitor_by_crate')
    # crate_code = models.ForeignKey(RearingMonitor, on_delete=models.CASCADE)
    harvest_date = models.DateTimeField()
    single_larvae = models.FloatField()
    starter_date = models.DateTimeField()
    # cage_code = models.ForeignKey(RearingMonitor, on_delete=models.CASCADE)
    cage_code = models.ForeignKey(RearingMonitor, on_delete=models.CASCADE, related_name='breedmonitor_by_cage')
    cage_date = models.DateTimeField()
    goal = models.CharField(max_length = 50)
    cage_geometry = models.FloatField()
    target_density = models.IntegerField()
    pupae = models.FloatField()
    amount_of_eggs = models.IntegerField()
    hydrogel_surface = models.CharField(max_length = 50)
    attractant = models.CharField(max_length = 50)
    first_emergence_date = models.DateTimeField()
    peak_daily = models.IntegerField()
    total_eggs_harvest = models.FloatField()
    avg_oviposition = models.IntegerField()
    oviposition = models.IntegerField()
    mg_eggs_female = models.FloatField()
    num_eggs_female = models.IntegerField()
    avg_fertility = models.IntegerField()
    num_clutches = models.IntegerField()
    num_females = models.IntegerField()
    from_hatch_to_emer_days = models.IntegerField()
    days_from_cage_date = models.DateTimeField()
    days_from_egg_placement = models.FloatField()
    days_for_first_egg_from_emer = models.FloatField()
    comments = models.CharField(max_length = 100)
