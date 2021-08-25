from typing import Any
import pytest
from django.db.utils import IntegrityError
from weather.models import Location, City, Country, Ocean


class TestLocation:
    def test_init(self, location_fake_data: dict[str, Any]) -> None:
        location: Location = Location(**location_fake_data)

        for field, value in location_fake_data.items():
            assert hasattr(location, field)
            assert isinstance(getattr(location, field), type(value))

    @pytest.mark.django_db
    def test_creation(
        self,
        location_fake_data: dict[str, Any],
        country_fake_data: dict[str, Any],
        city_fake_data: dict[str, Any],
        ocean_fake_data: dict[str, Any],
    ) -> None:
        country: Country = Country.objects.create(**country_fake_data)
        city: City = City.objects.create(**city_fake_data, country=country)
        ocean: Ocean = Ocean.objects.create(**ocean_fake_data)

        location: Location = Location.objects.create(
            **location_fake_data,
            city=city,
        )
        assert str(location) == f'{location.lat}, {location.lon}'

        location = Location.objects.create(
            **location_fake_data,
            ocean=ocean,
        )
        assert str(location) == f'{location.lat}, {location.lon}'

        with pytest.raises(IntegrityError):
            Location.objects.create(
                **location_fake_data,
                ocean=ocean,
                city=city,
            )

        with pytest.raises(IntegrityError):
            Location.objects.create(**location_fake_data)
