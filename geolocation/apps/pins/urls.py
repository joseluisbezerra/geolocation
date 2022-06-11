from django.urls import path

from geolocation.apps.pins import views

urlpatterns = [
    path('', views.home, name='home')
]
