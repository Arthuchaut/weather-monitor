from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from weather.models import Location, Weather
from weather.managers.measure_manager import MeasureManager


class Measure(models.Model):
    measure_id: models.BigAutoField = models.BigAutoField(
        primary_key=True, auto_created=True, serialize=False
    )
    measure_num: models.IntegerField = models.IntegerField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    measured_at: models.DateTimeField = models.DateTimeField()
    tz_timestamp: models.IntegerField = models.IntegerField()
    wind_speed: models.FloatField = models.FloatField()
    wind_deg: models.IntegerField = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(360),
        ]
    )
    wind_gust: models.FloatField = models.FloatField(null=True)
    visibility: models.IntegerField = models.IntegerField()
    temp: models.FloatField = models.FloatField()
    feels_like: models.FloatField = models.FloatField()
    temp_min: models.FloatField = models.FloatField()
    temp_max: models.FloatField = models.FloatField()
    pressure: models.IntegerField = models.IntegerField()
    humidity: models.IntegerField = models.IntegerField()
    sea_level: models.IntegerField = models.IntegerField(null=True)
    ground_level: models.IntegerField = models.IntegerField(null=True)
    weather: models.ForeignKey = models.ForeignKey(
        Weather, on_delete=models.CASCADE
    )
    location: models.ForeignKey = models.ForeignKey(
        Location, on_delete=models.CASCADE
    )

    objects: MeasureManager = MeasureManager()

    def __str__(self) -> str:
        return str(self.measure_id)

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'measure'
        verbose_name: str = _('measure')
        verbose_name_plural: str = _('measures')
