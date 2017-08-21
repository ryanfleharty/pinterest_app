from django import ModelForm
from .models import Pin, Board

class PinForm(ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'description', 'image']

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'description', 'image']