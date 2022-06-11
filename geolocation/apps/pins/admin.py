from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Pin


@admin.register(Pin)
class PinAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
