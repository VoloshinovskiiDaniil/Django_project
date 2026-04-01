from django.shortcuts import render, redirect
from .models import Country, UserCountry
from .forms import AddCountryForm

def home(request):
    return render(request, 'home.html')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'list_countries.html', { 'countries': countries })

def my_countries(request):
    countries = UserCountry.objects.all()
    return render(request, 'my_countries.html', {
        'countries': countries
    })

def country_add(request):
    form = AddCountryForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        country = Country.objects.get(name__iexact=name)

        if not UserCountry.objects.filter(country=country).exists():
            UserCountry.objects.create(country=country)

        return redirect('my_countries')

    return render(request, 'country_form.html', {'form': form})

def quiz(request):
    return render(request, 'quiz.html')
