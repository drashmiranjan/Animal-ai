from django import forms
from chat.models import *

class Animalform(forms.ModelForm):
    class Meta:
        model = AnimalModel
        fields = ['image']