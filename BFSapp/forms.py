# your_app/forms.py

from django import forms
from .models import EggMonitor
from django import forms

class EggMonitorForm(forms.ModelForm):
    class Meta:
        model = EggMonitor
        fields = ['date_measure', 'passed_hours', 'cage_code', 'egg_weight_1', 'egg_weight_2', 'egg_weight_3', 'num_eggs_1', 'num_eggs_2', 'num_eggs_3', 'total_eggs_weight', 'fertile_eggs_1', 'fertile_eggs_2', 'fertile_eggs_3', 'infertile_eggs_1', 'infertile_eggs_2', 'infertile_eggs_3', 'target_density', 'incubation_temp', 'incubation_tube', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make 'date_measure' and 'cage_code' read-only
        self.fields['date_measure'].widget.attrs['readonly'] = True
        self.fields['cage_code'].widget.attrs['readonly'] = True

class PredictionForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    humidity = forms.FloatField(label='Humidity')
    larvae_weight = forms.FloatField(label='Larvae Weight')
    num_of_pupae = forms.IntegerField(label='Number of Pupae')
    substrate_before_drying = forms.FloatField(label='Substrate Before Drying')
    substrate_after_drying = forms.FloatField(label='Substrate After Drying')
