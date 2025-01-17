
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cities/', views.city_index, name='city-index'),
    path('cities/<int:city_id>/', views.city_detail, name='city-detail'),
    path('cities/create/', views.CityCreate.as_view(), name='city-create'),
    path('cities/<int:pk>/update/', views.CityUpdate.as_view(), name='city-update'),
    path('cities/<int:pk>/delete/', views.CityDelete.as_view(), name='city-delete'),

    path('cities/<int:city_id>/add-attraction', views.add_attraction, name='add-attraction'),
    path('cities/<int:city_id>/attractions/<int:attraction_id>/', views.attraction_detail, name='attraction-detail'),

    path('bucketlists/', views.bucketlist_index, name='bucketlist-index'),
    path('bucketlists/<int:bucketlist_id>/', views.bucketlist_detail, name='bucketlist-detail'),

    path('accounts/signup/', views.signup, name='signup'),
]