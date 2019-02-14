from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.views.generic import FormView, TemplateView

from profiles.forms import SignUpForm


class SingUpFormView(FormView):
    form_class = SignUpForm
    template_name = 'profiles/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        # send email
        send_mail(
            'Welcome',
            'Registration completed',
            'gameshop@aalto.fi',
            [user.email]
        )
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class PurchasedGameView(TemplateView):
    template_name = 'profiles/purchased_games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = self.request.user.profile.games.all()
        return context
