from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView

from .models import City, Attraction
from .forms import AttractionForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

@login_required
def city_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

@login_required
def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    attraction_form = AttractionForm()
    return render(request, 'cities/detail.html', {'city': city, 'attraction_form': attraction_form})

class CityCreate(CreateView, LoginRequiredMixin):
    model = City
    fields = ['name', 'country', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CityUpdate(UpdateView, LoginRequiredMixin):
    model = City
    fields = ['country', 'description']

class CityDelete(DeleteView, LoginRequiredMixin):
    model = City
    success_url = '/cities/'

@login_required
def add_attraction(request, city_id):
    form = AttractionForm(request.POST)

    if form.is_valid():
        new_attraction = form.save(commit=False)
        new_attraction.city_id = city_id
        new_attraction.save()
    return redirect('city-detail', city_id=city_id)

@login_required
def attraction_detail(request, city_id, attraction_id):
    city = City.objects.get(id=city_id)
    attraction = Attraction.objects.get(id=attraction_id)
    return render(request, 'my_app/attraction_detail.html', {'city': city, 'attraction': attraction})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('city-index')
        else:
            error_message = 'Invalid sign up, please try again.'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

