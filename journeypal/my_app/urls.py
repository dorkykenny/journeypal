
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.city_index, name='city-index'),
    path('cities/<int:city_id>/', views.city_detail, name='city-detail'),
    path('cities/create/', views.CityCreate.as_view(), name='city-create'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='city-update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='city-delete'),
]