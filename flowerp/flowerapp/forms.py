from .models import Flower
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name','places', 'des', 'img']
