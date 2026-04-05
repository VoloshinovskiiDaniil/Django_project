import random
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


def modify_user_countries(request):
    action = request.POST.get('action')

    if action == 'add_world':
        countries = Country.objects.all()
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'add_europe':
        countries = Country.objects.filter(world_part__iexact='Europe')
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'add_asia':
        countries = Country.objects.filter(world_part__iexact='Asia')
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'add_africa':
        countries = Country.objects.filter(world_part__iexact='Africa')
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'add_america':
        countries = Country.objects.filter(world_part__iexact='America')
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'add_oceania':
        countries = Country.objects.filter(world_part__iexact='Oceania')
        for c in countries:
            UserCountry.objects.get_or_create(country=c)

    elif action == 'clear_world':
        UserCountry.objects.all().delete()

    elif action == 'clear_europe':
        UserCountry.objects.filter(country__world_part__iexact='Europe').delete()

    elif action == 'clear_asia':
        UserCountry.objects.filter(country__world_part__iexact='Asia').delete()

    elif action == 'clear_africa':
        UserCountry.objects.filter(country__world_part__iexact='Africa').delete()

    elif action == 'clear_america':
        UserCountry.objects.filter(country__world_part__iexact='America').delete()

    elif action == 'clear_oceania':
        UserCountry.objects.filter(country__world_part__iexact='Oceania').delete()

    return redirect('my_countries')


def quiz(request):
    user_countries = UserCountry.objects.all()

    if not user_countries.exists():
        return render(request, 'quiz.html', {
            'error': 'No countries in your list!'
        })

    if request.method == 'GET':
        country = random.choice([uc.country for uc in user_countries])
        hints = []
        message = None

    else:
        country_id = request.POST.get('country_id')
        country = Country.objects.get(id=country_id)

        hints = request.POST.getlist('hints')
        message = None

    if 'next' in request.POST:
        country = random.choice([uc.country for uc in user_countries])
        hints = []
        message = None

    elif 'hint' in request.POST:
        hint = request.POST.get('hint')
        if hint not in hints:
            hints.append(hint)

    elif 'answer' in request.POST:
        answer = request.POST.get('answer', '').strip()

        if answer.lower() == country.name.lower():
            message = "Correct!"
        else:
            message = f"Wrong! It was {country.name}"

    return render(request, 'quiz.html', {
        'country': country,
        'hints': hints,
        'message': message
    })
