
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.city_index, name='city-index'),
        path('cities/<int:city_id>/', views.city_detail, name='city-detail'),
]