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
    sample_day = forms.IntegerField(min_value=1, max_value=14, required=True, label='Sample Day')
    temperature = forms.IntegerField(min_value=25, max_value=65, required=True, label='Temperature')
    humidity = forms.IntegerField(min_value=30, max_value=100, required=True, label='Humidity')
    larvae_weight = forms.FloatField(min_value=0.01, required=True, label='Larvae Weight')
    num_of_pupae = forms.IntegerField(min_value=1, required=True, label='Number of Pupae')
    substrate_before_drying = forms.FloatField(min_value=0.01, required=True, label='Substrate Before Drying')
    substrate_after_drying = forms.FloatField(min_value=0.01, required=True, label='Substrate After Drying')
