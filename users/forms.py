from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class DateInput(forms.DateInput):
    input_type = 'date'

class  UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
	# birth_date = forms.DateField()
	class Meta:
		model = Profile
		fields = ['image', 'birth_date', 'address', 'contact_number']
		widgets = {
            'birth_date': DateInput(),
        }