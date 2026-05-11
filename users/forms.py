from django import forms
from . import models
class UserForm(forms.ModelForm):
    class Meta:
        model=models.ControlUsers
        fields = ['first_name', 'last_name','age', 'email', 'phon','avatar']
        

    