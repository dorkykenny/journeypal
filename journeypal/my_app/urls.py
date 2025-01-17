
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.city_index, name='city-index'),
]