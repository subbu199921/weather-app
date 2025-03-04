from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_location, name='search_location'),
]