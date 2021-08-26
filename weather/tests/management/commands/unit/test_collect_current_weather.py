from typing import Any
import pytest
from _pytest.monkeypatch import MonkeyPatch
from django.core.management import call_command
from weather.management.commands.collect_current_weather import Command
from weather.libs.api.open_weather_map import OpenWeatherMap
from weather.models import Measure


class TestCollectCurrentWeather:
    @pytest.mark.django_db
    def test_handle(
        self,
        current_weather_fake_data: list[dict[str, Any]],
        fake_owm: OpenWeatherMap,
        monkeypatch: MonkeyPatch,
    ) -> None:
        call_command('loaddata', 'weather/models/data/country_data.json')

        def get_weather_by_coord_patch(
            self, lat: float, lon: float
        ) -> dict[str, Any]:
            for measure in current_weather_fake_data:
                if (measure['coord']['lat'], measure['coord']['lon']) == (
                    lat,
                    lon,
                ):
                    return measure

        monkeypatch.setattr(
            OpenWeatherMap, 'get_weather_by_coord', get_weather_by_coord_patch
        )
        command: Command = Command()
        command.handle()

        for measure in current_weather_fake_data:
            Measure.objects.get(
                location__lat=measure['coord']['lat'],
                location__lon=measure['coord']['lon'],
            )
