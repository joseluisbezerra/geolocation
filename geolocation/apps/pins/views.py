from datetime import date

from django.contrib.gis.db.models.functions import AsGeoJSON
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

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
            'id',
            'name',
            'expiration_date',
            'pin_location'
        )
    )

    return JsonResponse(pins, safe=False)


def delete_pin(request, id):
    pin = get_object_or_404(Pin, pk=id)

    pin.delete()

    messages.success(request, 'Successfully deleted pin')

    return redirect('/')
