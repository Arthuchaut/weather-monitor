from typing import Any
import pytest
from weather.models import Weather


class TestCity:
    def test_init(self, weather_fake_data: dict[str, Any]) -> None:
        weather: Weather = Weather(**weather_fake_data)

        for field, value in weather_fake_data.items():
            assert hasattr(weather, field)
            assert isinstance(getattr(weather, field), type(value))

    @pytest.mark.django_db
    def test_creation(self, weather_fake_data: dict[str, Any]) -> None:
        weather: Weather = Weather.objects.create(**weather_fake_data)
        assert str(weather) == weather_fake_data['state']
