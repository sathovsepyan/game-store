from django import forms

from categories.models import Category


class GameSearchForm(forms.Form):
    title = forms.CharField(required=False)
    category = forms.TypedMultipleChoiceField(
        required=False,
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control mb-2 mr-sm-2',
            'placeholder': 'Game title'
        }

        self.fields['category'].widget.attrs = {
            'class': 'form-control mb-2 mr-sm-2',
        }
        categories_choices = [
            (category['slug'], category['title'])
            for category in Category.objects.values('title', 'slug')
        ]

        self.fields['category'].choices = categories_choices
