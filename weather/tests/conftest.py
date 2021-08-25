from typing import Any
import pytest


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
