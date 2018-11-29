from django import forms
from .models import Presents

class PresentsModelForm(forms.ModelForm):
    class Meta:
        model = Presents
        fields=[
            'title',
            'memento',
            'given_to',
            'type_input',
            'created_at',
            'given_at'
        ]