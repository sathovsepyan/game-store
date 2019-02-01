from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.ModelForm):
    role = forms.ChoiceField(choices=[
        ('dev', 'developer'),
        ('player', 'player')
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Email'
        }

        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'First name'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Second name'
        }
        self.fields['role'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
        ]


class SignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Email address'
        }

        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }