from .models import contact
from django import forms

class contact_form(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','msg']


