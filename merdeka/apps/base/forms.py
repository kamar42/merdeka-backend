from django import forms
from django.core.exceptions import MultipleObjectsReturned
from .models import MyUser

class LoginForm(forms.Form):
    username = forms.RegexField(label=("Username"), max_length=100, regex=r'^[\w.@+-]+$', help_text=("Field cannot be empty. Max, 30 character. Only contain letter, number, and @/./+/-/_."), error_messages={'invalid': ("Invalid, should only contain letter, number and @/./+/-/_.")})
    password = forms.CharField(required=True, widget=forms.PasswordInput)
