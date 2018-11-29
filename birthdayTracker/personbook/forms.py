from django import forms
from .models import Personbooks

class PersonsModelForm(forms.ModelForm):
    class Meta:
        model = Personbooks
        fields=[
            'title',
            'created_at',
            'lastName',
            'firstName',
            'relation',
            'birthday',
        ]