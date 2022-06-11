from django.contrib.gis.db import models


class Pin(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    expiration_date = models.DateField()

    class Meta:
        db_table = 'pin'

    def __str__(self) -> str:
        return self.name
