from django.views.generic import FormView

from profiles.models import Profile
from profiles.forms import SignUpForm


class SingUpFormView(FormView):
    form_class = SignUpForm
    template_name = 'profiles/signup.html'
    success_url = '/'

    def form_invalid(self, form):
        print('@@@@@@@@@')
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.save()

        Profile.objects.create(
            user=user,
            role=form.cleaned_data.get('role')
        )
        return super().form_valid(form)
