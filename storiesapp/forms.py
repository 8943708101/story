from . models import Mystory
from django import forms
class Storiesforms(forms.ModelForm):
    class Meta:
        model=Mystory
        fields=['name','desc','date']
