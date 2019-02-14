from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from profiles.models import Profile


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('developer', 'developer'),
        ('player', 'player')
    ])

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['role'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })

    def save(self, commit=True):
        user = super().save(commit)
        user.email = self.cleaned_data.get('email')
        user.save()

        Profile.objects.create(
            user=user,
            role=self.cleaned_data['role']
        )
        return user

    # class Meta:
    #     model = User
    #     fields = [
    #         'email',
    #         'password',
    #         'first_name',
    #         'last_name',
    #     ]


class SignInForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Username'
        }

        self.fields['password'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
        }
