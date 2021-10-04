from django import forms
from .models import *

class GestionForm(forms.ModelForm):
    class Meta:
        model = Gestion
        fields = '__all__'