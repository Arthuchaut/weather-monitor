from typing import Any
import pytest
from weather.models import Country


class TestCountry:
    def test_init(self, country_fake_data: dict[str, Any]) -> None:
        country: Country = Country(**country_fake_data)

        for field, value in country_fake_data.items():
            assert hasattr(country, field)
            assert isinstance(getattr(country, field), type(value))

    @pytest.mark.django_db
    def test_creation(self, country_fake_data: dict[str, Any]) -> None:
        country: Country = Country.objects.create(**country_fake_data)
        assert str(country) == country_fake_data['name']
