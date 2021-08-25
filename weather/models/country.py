from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    country_id: models.BigAutoField = models.BigAutoField(
        primary_key=True, auto_created=True, serialize=False
    )
    country_code: models.CharField = models.CharField(max_length=2)
    name: models.CharField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'country'
        verbose_name: str = _('country')
        verbose_name_plural: str = _('countries')
