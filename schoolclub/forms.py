from django import forms
from .models import Universities
from django.forms import ModelForm, DateInput, TextInput, NumberInput

class UNiversities_form(forms.ModelForm):
    class Meta:
        model = Universities
        fields = ('name', 'last_name','date', 'phone')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Example: Sherlock', 'id':'namel'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Example: Holmes'
            }),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'size':'16', 'id':'datetime'
            }),
            'phone': NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Example: +7 777 777 7777', 'type':'Number'
            })
        }