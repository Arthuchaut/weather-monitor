from typing import Any
import pytest
from weather.models import City, Country


class TestCity:
    def test_init(self, city_fake_data: dict[str, Any]) -> None:
        city: City = City(**city_fake_data)

        for field, value in city_fake_data.items():
            assert hasattr(city, field)
            assert isinstance(getattr(city, field), type(value))

    @pytest.mark.django_db
    def test_creation(
        self, city_fake_data: dict[str, Any], country_fake_data: dict[str, Any]
    ) -> None:
        country: Country = Country.objects.create(**country_fake_data)
        city: City = City.objects.create(**city_fake_data, country=country)
        assert str(city) == city_fake_data['name']
