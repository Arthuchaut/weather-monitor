from django.db import models
from django.utils.translation import gettext_lazy as _


class Ocean(models.Model):
    ocean_id: models.BigAutoField = models.BigAutoField(
        primary_key=True,
        auto_created=True,
        serialize=False,
    )
    name: models.CharField = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        app_label: str = 'weather'
        db_table: str = 'ocean'
        verbose_name: str = _('ocean')
        verbose_name_plural: str = _('oceans')
