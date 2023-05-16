from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.forms import ModelForm

from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input", 'placeholder': 'Введите имя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": 'input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input", 'placeholder': 'Введите имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input", 'placeholder': 'Введите почту'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите новое имя'}))
    password = None
    new_password1 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Повторите новый пароль'}))

    class Meta:
        model = User
        fields = ['username', 'new_password1', 'new_password2']

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error("new_password2", "Пароли не совпадают")

class RecordForm(ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    temperature = forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Введите температуру'}))
    class Meta:
        model = Measurements
        fields = ["city", "device", "temperature"]