# your_app/forms.py

from django import forms
from .models import EggMonitor

class EggMonitorForm(forms.ModelForm):
    class Meta:
        model = EggMonitor
        fields = ['date_measure', 'passed_hours', 'cage_code', 'egg_weight_1', 'egg_weight_2', 'egg_weight_3', 'num_eggs_1', 'num_eggs_2', 'num_eggs_3', 'total_eggs_weight', 'fertile_eggs_1', 'fertile_eggs_2', 'fertile_eggs_3', 'infertile_eggs_1', 'infertile_eggs_2', 'infertile_eggs_3', 'target_density', 'incubation_temp', 'incubation_tube', 'comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Make 'date_measure' and 'cage_code' read-only
        self.fields['date_measure'].widget.attrs['readonly'] = True
        self.fields['cage_code'].widget.attrs['readonly'] = True
