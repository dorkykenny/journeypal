from django.shortcuts import render
from .models import City
def home(request):
    return render(request, 'home.html')

def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})