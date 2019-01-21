from django.views.generic import FormView

from profiles.forms import SignUpForm


class SingUpFormView(FormView):
    form_class = SignUpForm
    template_name = 'profiles/signup.html'
    success_url = '/'
