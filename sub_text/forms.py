from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
"""
class userform(forms.ModelForm):
	username = forms.CharField(label='Username', widget=forms.TextInput(
		attrs={'class':'form-control','placeholder': 'Enter Name Here PLZ', 'name':'nm','id':'d1'}), required=True, max_length=100)
	email = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=100)

	first_name = forms.CharField(label='Firstname', widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Firstname', 'id':'d1'}), required=True, max_length=100)
	last_name = forms.CharField(label='Lastname', widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Lastname', 'id':'d1'}), required=True, max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
	confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)

	class Meta():
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
"""
class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200)


	class meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class loginform(forms.ModelForm):
	name = forms.CharField(label='Enter username', widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Enter Name Here PLZ', 'id':'d1'}), required=True, max_length=100)
	password = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

	class Meta():
		model = User
		fields = ['name', 'password']
		
	
FRUIT_CHOICES= [ ('orange', 'Oranges'),('cantaloupe', 'Cantaloupes'),
('mango', 'Mangoes'),('honeydew', 'Honeydews'), ]
OPTIONS = ( ("AUT", "Austria"),("DEU", "Germany"),("NLD", "Neitherlands"),)
CHOICES=[('select1','select 1'),('select2','select 2')]

class studentform(forms.ModelForm):
	name = forms.CharField(label='enter name',widget=forms.TextInput(
	attrs={'class':'form-control','placeholder':'Enter Name Here PLZ','id':'d1'}
	),required=True,max_length=100)
	email = forms.EmailField(widget=forms.EmailInput(),required=True,max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(), required=True,
	max_length=100)
	city = forms.CharField(widget=forms.TextInput(),required=False,max_length=100)
	marks = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
	favorite_fruit = forms.ChoiceField(label='What is your favorite fruit?',
	initial='mango',widget=forms.RadioSelect,choices=FRUIT_CHOICES)
	Countries = forms.MultipleChoiceField(label='Your Country?', initial='DEU',
	widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
	fruits = forms.CharField(label='What is your favorite fruit?',initial='mango',
	widget=forms.Select(choices=FRUIT_CHOICES))
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':3}),
	required=True, max_length=10)
	docfile = forms.FileField()
	class Meta():
		model = student
		fields = ['name','email','password','city','marks','favorite_fruit','Countries','comment','fruits','docfile']
		
		