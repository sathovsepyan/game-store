from django import forms

from games.models import Game


class CreateGameForm(forms.ModelForm):
    fields = ['title', 'url', 'description', 'price', 'category', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control'
            }

    class Meta:
        model = Game
        fields = ['title', 'url', 'description', 'price', 'category', 'thumbnail']
