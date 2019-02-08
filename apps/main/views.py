from django.views.generic import ListView

from games.models import Game
from django.shortcuts import render, get_object_or_404

from main.forms import GameSearchForm

# TODO: Move from the main app the 'playgame' method to another app that deals the display of the game.
def playgame(request, game_id):
    obj = get_object_or_404(Game, pk=game_id)
    return  render(request, 'main/gamecontainer.html', {'game': obj})
    
class IndexPageView(ListView):
    template_name = 'main/index.html'
    queryset = Game.objects.filter(is_deleted=False)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('title'):
            qs = qs.filter(title__contains=self.request.GET.get('title'))
        if self.request.GET.get('category'):
            qs = qs.filter(category__slug__in=self.request.GET.getlist('category'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = GameSearchForm(data=self.request.GET or None)
        return context


