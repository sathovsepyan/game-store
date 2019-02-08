from django.views.generic import FormView, TemplateView

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
        form.save()
        return super().form_valid(form)


class PurchasedGameView(TemplateView):
    template_name = 'profiles/purchased_games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['games'] = self.request.user.profile.games.all()
        return context
