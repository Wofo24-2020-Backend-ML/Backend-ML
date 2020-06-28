from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from account.models import Professional


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['phone_no', 'sub_category', 'business_name', 'address', 'service_charge', 'logo']
        labels = {
            'sub_category': 'Select Skills'
        }

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']