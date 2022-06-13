from datetime import date

from django.contrib.gis.db.models.functions import AsGeoJSON
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from geolocation.apps.pins.forms import PinForm

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


def new_pin(request):
    if (request.method == 'POST'):
        form = PinForm(request.POST)

        if (form.is_valid()):
            form.save()

            messages.success(request, 'Pin added successfully')

            return redirect(reverse('home'))
        else:
            messages.error(request, form.errors)

            return redirect(reverse('new_pin'))
    else:
        form = PinForm()

        return render(request, 'pins/add_pin.html', {'form': form})


def edit_pin(request, id):
    pin = get_object_or_404(Pin, pk=id)

    if (request.method == 'POST'):
        form = PinForm(request.POST, instance=pin)

        if (form.is_valid()):
            form.save()
            messages.success(request, 'Pin edited successfully.')

            return redirect(reverse('home'))
        else:
            return render(
                request,
                'pins/edit_pin.html',
                {'form': form, 'pin': pin}
            )
    else:
        form = PinForm(instance=pin)

        return render(
            request,
            'pins/edit_pin.html',
            {'form': form, 'pin': pin}
        )


def delete_pin(request, id):
    pin = get_object_or_404(Pin, pk=id)

    pin.delete()

    messages.success(request, 'Successfully deleted pin')

    return redirect(reverse('home'))
