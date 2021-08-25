from django.db import models
from weather.models import City, Ocean


class LocationManager(models.Manager):
    def create(
        self,
        lat: float,
        lon: float,
        city: City = None,
        ocean: Ocean = None,
    ) -> object:
        if not city and not ocean or city and ocean:
            raise ValueError(
                'Only one of the city or ocean object must be given.'
            )

        location: self.model = self.model(
            lat=lat,
            lon=lon,
            city=city,
            ocean=ocean,
        )
        location.save(using=self._db)

        return location
