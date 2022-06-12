from django.urls import path

from geolocation.apps.pins import views

urlpatterns = [
    path('', views.home, name='home'),

    path('pins/', views.pins_list, name='pins_list'),

    path('delete/<int:id>/', views.delete_pin, name='delete_pin')
]
