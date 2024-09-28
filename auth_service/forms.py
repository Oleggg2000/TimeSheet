"""Customizing form inputs"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserAccount


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(
        widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'id': "username", 'name': "username"}))

    class Meta:
        model = UserAccount
        fields = ('password', 'username')


class UserRegistrationForm(UserCreationForm):
    usable_password = None
    username = forms.CharField(widget=forms.TextInput(), help_text='Username')
    first_name = forms.CharField(widget=forms.TextInput(), help_text='First Name')
    last_name = forms.CharField(widget=forms.TextInput(), help_text='Last Name')
    birthday = forms.CharField(widget=forms.DateTimeInput(), help_text='Birthday', required=False)
    email = forms.EmailField(widget=forms.EmailInput(), help_text='Email', required=False)
    phone_number = forms.CharField(widget=forms.TextInput(), help_text='Phone Number', required=False)
    vk_id = forms.CharField(widget=forms.TextInput(), help_text='VK id', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text='Confirm Password')

    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'phone_number', 'vk_id', 'password1',
                  'password2')
