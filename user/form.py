from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class SignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'required': 'Username is required.'}
        self.fields['password1'].error_messages = {'required': 'password is required.'}

    username = forms.EmailField(
        max_length=30,
        required=True,
        help_text='Optional.',
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'input-text full-width email', 'autocapitalize': 'off',
                   'placeholder': 'Email', 'autofocus': 'autofocus', 'type': 'text'})
    )

    first_name = forms.CharField(
        max_length=30, 
        required=False, 
        help_text='Optional.',
        widget=forms.TextInput(attrs={'autofocus': True,'class' : 'input-text full-width email', 'autocapitalize':'off', 'placeholder':'Firstname', 'autofocus':'autofocus', 'type':'text'})
    )

    last_name = forms.CharField(
        max_length=30, 
        required=False, 
        help_text='Optional.',
        widget=forms.TextInput(attrs={'autofocus': True,'class' : 'input-text full-width email', 'autocapitalize':'off', 'placeholder':'Lastname', 'autofocus':'autofocus', 'type':'text'})
    )

    mobile_no = forms.CharField(
        max_length=30,
        required=False,
        help_text='Optional.',
        widget=forms.TextInput(attrs={'class' : 'input-text full-width email', 'autocapitalize':'off', 'placeholder':'Mobile no', 'autofocus':'autofocus', 'type':'text'})
    )

    password1 = forms.CharField(
        label=_("Password"),
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input-text full-width password', 'placeholder': 'Password', 'type': 'password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name','password1', "mobile_no")

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True,'class' : 'input-text full-width email', 'spellcheck':'false',  'autocorrect':'off', 'autocapitalize':'off', 'placeholder':'Email', 'autofocus':'autofocus', 'type':'email'}),
    )
    
    password = forms.CharField(
    label=_("Password"),
    strip=False,
    widget=forms.PasswordInput(attrs={'class' : 'input-text full-width password','placeholder':'Password', 'type':'password'}),
    )