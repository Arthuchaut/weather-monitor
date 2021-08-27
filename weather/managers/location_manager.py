from django.db import models
from django.db.utils import IntegrityError
from weather.models import City, Ocean


class LocationManager(models.Manager):
    '''The location management class.'''

    def create(
        self,
        lat: float,
        lon: float,
        city: City = None,
        ocean: Ocean = None,
    ) -> object:
        '''Create and save a new Location according to the
        foreign key integrity constraint.

        Args:
            lat (float): The latitude.
            lon (float): The longitude.
            city (City): The city to relate. Default to None.
            ocean (Ocean): The ocean to relate. Default to None.

        Raises:
            IntegrityError: If the constraint is not respected.

        Returns:
            Location: The new Location registered.
        '''

        if not city and not ocean or city and ocean:
            raise IntegrityError(
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
