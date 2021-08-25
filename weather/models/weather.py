from django.db import models
from django.utils.translation import gettext_lazy as _


class Weather(models.Model):
    weather_id: models.BigAutoField = models.BigAutoField(
        primary_key=True, serialize=False
    )
    state: models.CharField = models.CharField(max_length=255)
    description: models.TextField = models.TextField()

    def __str__(self) -> str:
        return self.state

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'weather'
        verbose_name: str = _('weather')
        verbose_name_plural: str = _('weathers')
