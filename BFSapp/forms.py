from django import forms

class PredictionForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    humidity = forms.FloatField(label='Humidity')
    larvae_weight = forms.FloatField(label='Larvae Weight')
    num_of_pupae = forms.IntegerField(label='Number of Pupae')
    substrate_before_drying = forms.FloatField(label='Substrate Before Drying')
    substrate_after_drying = forms.FloatField(label='Substrate After Drying')
