from django import forms
from .models import Country

class AddCountryForm(forms.Form):
    name = forms.CharField(label="Name of a country", max_length=100)

    def clean_name(self):
        name = self.cleaned_data['name']

        if not Country.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("No such country in the database")

        return name