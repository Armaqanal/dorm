from .models import Customer, Manager, User
from django import forms


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'



