from datetime import date

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.gis.db.models.functions import AsGeoJSON

from geolocation.apps.pins.models import Pin


def home(request):
    return render(request, 'pins/home.html')


def pins_list(request):
    pins = list(
        Pin.objects.filter(
            expiration_date__gte=date.today()
        ).annotate(
            pin_location=AsGeoJSON('location')
        ).values(
            'name',
            'pin_location'
        )
    )

    return JsonResponse(pins, safe=False)
