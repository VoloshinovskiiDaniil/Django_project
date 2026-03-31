from django.shortcuts import render
from .models import Country

def home(request):
    return render(request, 'home.html')

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'list.html', { 'countries': countries })

def country_add(request):
    return render(request, 'form.html')

def quiz(request):
    return render(request, 'quiz.html')
