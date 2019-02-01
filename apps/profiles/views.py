from django.views.generic import FormView, TemplateView

from profiles.models import Profile
from profiles.forms import SignUpForm
from games.models import Game


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


class PurchasedGameView(TemplateView):
    template_name = 'profiles/purchased_games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = self.request.user.profile.games.all()
        return context