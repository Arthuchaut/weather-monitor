from typing import Any
import pytest
from django.utils import timezone
from weather.libs.api.open_weather_map import OpenWeatherMap


@pytest.fixture
def country_fake_data() -> dict[str, Any]:
    return {
        'name': 'France',
        'country_code': 'FR',
    }


@pytest.fixture
def city_fake_data() -> dict[str, Any]:
    return {
        'city_id': 123456,
        'name': 'Rennes',
    }


@pytest.fixture
def ocean_fake_data() -> dict[str, Any]:
    return {
        'name': 'Atlantic Ocean',
    }


@pytest.fixture
def location_fake_data() -> dict[str, Any]:
    return {
        'lat': 48.10618240499252,
        'lon': -1.6479917725717026,
    }


@pytest.fixture
def weather_fake_data() -> dict[str, Any]:
    return {
        'weather_id': 123456,
        'state': 'Cloudy',
        'description': 'It\'s means that\'s cloudy bro.',
    }


@pytest.fixture
def measure_fake_data() -> dict[str, Any]:
    return {
        'measure_num': 1,
        'created_at': timezone.now(),
        'measured_at': timezone.now(),
        'tz_timestamp': -43000,
        'wind_speed': 42.8,
        'wind_deg': 45,
        'wind_gust': 45.2,
        'visibility': 1000,
        'temp': 14.5,
        'feels_like': 12.14,
        'temp_min': 8.6,
        'temp_max': 14.5,
        'pressure': 10,
        'humidity': 5,
        'sea_level': 10,
        'ground_level': 12,
    }


@pytest.fixture
def fake_token() -> str:
    return 'abcdefghijklmnopqrstuvw'


@pytest.fixture
def fake_owm(fake_token: str) -> OpenWeatherMap:
    return OpenWeatherMap(token=fake_token, calls_per_min=4)
