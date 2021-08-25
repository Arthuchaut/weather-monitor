from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from weather.models import City, Ocean
from weather.managers import LocationManager


class Location(models.Model):
    location_id: models.BigAutoField = models.BigAutoField(
        primary_key=True, auto_created=True, serialize=False
    )
    lat: models.FloatField = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    lon: models.FloatField = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    city: models.ForeignKey = models.ForeignKey(
        City, on_delete=models.CASCADE, null=True
    )
    ocean: models.ForeignKey = models.ForeignKey(
        Ocean, on_delete=models.CASCADE, null=True
    )

    objects: LocationManager = LocationManager()

    def __str__(self) -> str:
        return f'{self.lat}, {self.lon}'

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'location'
        verbose_name: str = _('location')
        verbose_name_plural: str = _('locations')
