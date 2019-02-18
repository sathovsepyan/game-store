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
            'class': 'form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0 col-xs-4 col-md-6',
            'placeholder': 'Search by game title'
        }
        
        self.fields['category'].widget.attrs = {
            'class': 'selectpicker form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0 col-xs-4 col-md-3 categories-align',
            'data-live-search-normalize': 'true',
            'data-live-search': 'true',
            'data-container': 'body',
            'data-header': 'Categories',
            'max-options-text': 'All',
            'title': 'Select categories'
        }
        categories_choices = [
            (category['slug'], category['title'])
            for category in Category.objects.values('title', 'slug')
        ]

        self.fields['category'].choices = categories_choices
