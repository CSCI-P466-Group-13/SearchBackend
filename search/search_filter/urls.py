from django.urls import path
from . import views
from .views import property_list
from .views import vehicle_list
from .views import all_list

urlpatterns = [
    path("",views.index, name="index"),
    path("search/", views.search, name="search"),
    path('api/properties', property_list, name='property_list'),
    path('api/vehicles', vehicle_list, name='vehicle_list'),
    path('api/all', all_list, name='all_list'),
]