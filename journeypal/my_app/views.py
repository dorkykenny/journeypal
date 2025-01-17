from django.shortcuts import render
from .models import City
def home(request):
    return render(request, 'home.html')

def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'cities/detail.html', {'city': city})