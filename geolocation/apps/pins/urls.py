from django.urls import path

from geolocation.apps.pins import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pins/', views.pins_list, name='pins_list')
]
