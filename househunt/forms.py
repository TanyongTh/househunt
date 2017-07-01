from django import forms

from .models import Property


class ScrapingForm(forms.Form):
    url = forms.CharField(200)

class SearchForm(forms.Form):
    address = forms.CharField(max_length=200, required=False)
    postcode = forms.CharField(max_length=4, required=False)