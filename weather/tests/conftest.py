from typing import Any
import pathlib
import json
import pytest
from _pytest.monkeypatch import MonkeyPatch
from django.utils import timezone
from django.conf import settings
from weather.libs.api.open_weather_map import OpenWeatherMap
from weather.libs.api.request_flow_controller import RequestFlowController


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
def current_weather_fake_data() -> list[dict[str, Any]]:
    data: list[dict[str, Any]] = json.loads(
        (
            settings.BASE_DIR
            / 'weather'
            / 'tests'
            / '__samples__'
            / 'weather_fake_data.json'
        ).read_text()
    )
    return data


@pytest.fixture
def fake_token() -> str:
    return 'abcdefghijklmnopqrstuvw'


@pytest.fixture
def fake_owm(
    fake_token: str, tmp_path: pathlib.Path, monkeypatch: MonkeyPatch
) -> OpenWeatherMap:
    monkeypatch.setattr(settings, 'BASE_DIR', tmp_path)
    return OpenWeatherMap(token=fake_token, calls_per_min=4)
