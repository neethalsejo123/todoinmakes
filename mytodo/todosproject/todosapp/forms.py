from .models import Taskt
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Taskt
        fields=['name','priority','date']
