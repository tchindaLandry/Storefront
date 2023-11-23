# forms.py
from django import forms

class LocationForm(forms.Form):
    location_name = forms.CharField(max_length=255)