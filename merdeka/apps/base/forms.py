from django import forms
from django.core.exceptions import MultipleObjectsReturned
from .models import MyUser

class LoginForm(forms.Form):
    username = forms.RegexField(label=("Username"), max_length=100, regex=r'^[\w.@+-]+$', help_text=("Field cannot be empty. Max, 30 character. Only contain letter, number, and @/./+/-/_."), error_messages={'invalid': ("Invalid, should only contain letter, number and @/./+/-/_.")})
    password = forms.CharField(required=True, widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    """
    Form that used to represent sign up form. There are three inputs username, email, and password.
    """

    error_messages = {
        'duplicate_username': ("Username not avalaible."),
        'duplicate_email': ("Email not avalaible."),
    }

    username = forms.RegexField(label=("Username"), max_length=30, regex=r'^[\w.@+-]+$',
                                help_text=("*Required. Max 30 character. Can only contain letters, number and @/./+/-/_."),
                                error_messages={'invalid': ("Can only contain letters, number and "
                                                            "@/./+/-/_.")})
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            MyUser._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM.
        email = self.cleaned_data["email"]
        try:
            MyUser._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        except MultipleObjectsReturned:
            pass
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
