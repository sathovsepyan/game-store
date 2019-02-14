from django import forms

from categories.models import Category


class GameSearchForm(forms.Form):
    title = forms.CharField(required=False)
    category = forms.TypedMultipleChoiceField(
        required=False,
        choices=[]
    )
    choices = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control mb-2 mr-sm-4 col-lg-3 col-md-6',
            'placeholder': 'Game title'
        }

        self.fields['category'].widget.attrs = {
            'class': 'form-control mb-2 mr-sm-4 col-lg-3 col-md-6',
        }
        self.choices = [
            (category['slug'], category['title'])
            for category in Category.objects.values('title', 'slug')
        ]

        self.fields['category'].choices = self.choices
