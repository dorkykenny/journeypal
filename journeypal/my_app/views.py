from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import City


def home(request):
    return render(request, 'home.html')

def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'cities/detail.html', {'city': city})

class CityCreate(CreateView):
    model = City
    fields = '__all__'
    success_url = '/cities/'

class CityUpdate(UpdateView):
    model = City
    fields = ['country', 'description']

class CityDelete(DeleteView):
    model = City
    success_url = '/cities/'