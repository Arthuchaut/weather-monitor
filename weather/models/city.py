from django.db import models
from django.utils.translation import gettext_lazy as _
from weather.models import Country


class City(models.Model):
    city_id: models.BigAutoField = models.BigAutoField(
        primary_key=True, serialize=False
    )
    name: models.CharField = models.CharField(max_length=255)
    country: models.ForeignKey = models.ForeignKey(
        Country, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'city'
        verbose_name: str = _('city')
        verbose_name_plural: str = _('cities')
