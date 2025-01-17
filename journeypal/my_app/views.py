from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import City, Attraction
from .forms import AttractionForm


def home(request):
    return render(request, 'home.html')

def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    attraction_form = AttractionForm()
    return render(request, 'cities/detail.html', {'city': city, 'attraction_form': attraction_form})

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

def add_attraction(request, city_id):
    form = AttractionForm(request.POST)

    if form.is_valid():
        new_attraction = form.save(commit=False)
        new_attraction.city_id = city_id
        new_attraction.save()
    return redirect('city-detail', city_id=city_id)

class AttractionDetail(DetailView):
    model = Attraction