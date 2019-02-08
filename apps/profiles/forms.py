from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from profiles.models import Profile


class SignUpForm(forms.ModelForm):
    role = forms.ChoiceField(choices=[
        ('developer', 'developer'),
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

    def save(self, commit=False):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        Profile.objects.create(
            user=user,
            role=self.cleaned_data['role']
        )
        return user

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
