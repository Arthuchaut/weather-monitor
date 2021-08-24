from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    country_code: models.CharField = models.CharField(max_length=2)
    name: models.CharField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'weather'
        verbose_name: str = _('weather')
        verbose_name_plural: str = _('weathers')
