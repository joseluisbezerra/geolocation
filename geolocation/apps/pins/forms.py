from datetime import date

from django.contrib.gis import forms
from django.core.exceptions import ValidationError

from geolocation.apps.pins.models import Pin


class PinForm(forms.ModelForm):
    location = forms.PointField(
        srid=4326,
        widget=forms.OSMWidget(
            attrs={
                "map_width": 800,
                "map_srid": 4326,
                "map_height": 500,
                "default_zoom": 7,
            }
        ),
    )

    class Meta:
        model = Pin
        fields = ('location', 'name', 'expiration_date')
        widgets = {
            'expiration_date': forms.TextInput(
                attrs={'type': 'date'}
            )
        }

    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']

        if expiration_date < date.today():
            raise ValidationError("Expiration date cannot be less than today.")

        return expiration_date
