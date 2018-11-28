from django import forms
from .models import Yearbooks

class YearbookModelForm(forms.ModelForm):
    class Meta:
        model = Yearbooks
        fields=[
            'title',
        ]