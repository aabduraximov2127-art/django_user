from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.ControlUsers
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'phon',
            'avatar'
        ]


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Parol"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Parolni tasdiqlang"
        })
    )

    class Meta:
        model = models.ControlUsers
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'phon',
            'avatar'
        ]

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Parollar mos emas!")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Parol"
        })
    )