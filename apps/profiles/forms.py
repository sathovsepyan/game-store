from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    role = forms.ChoiceField(choices=[
        ('dev', 'developer'),
        ('player', 'player')
    ])

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
        ]
