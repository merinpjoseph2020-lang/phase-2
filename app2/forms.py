from .models import contact
from django import forms

class contact_form(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','email','msg']


from django import forms
from .models import Billing

class DeliveryDetailsForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['mobile', 'alternate', 'house', 'street', 'city', 'state', 'pincode', 'landmark']
