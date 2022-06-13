from django.urls import path

from geolocation.apps.pins import views

urlpatterns = [
    path('', views.home, name='home'),

    path('pins/', views.pins_list, name='pins_list'),
    path('pins/new/', views.new_pin, name='new_pin'),
    path('pins/<int:id>/edit/', views.edit_pin, name='edit_pin'),
    path('pins/<int:id>/delete/', views.delete_pin, name='delete_pin')
]
