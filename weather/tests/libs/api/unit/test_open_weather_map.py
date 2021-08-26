from typing import Any
import requests
import pytest
from _pytest.monkeypatch import MonkeyPatch
from unittest.mock import Mock
from weather.libs.api.open_weather_map import OpenWeatherMap
from weather.libs.api.request_flow_controller import RequestFlowController


class TestOpenWeatherMap:
    def test_init(self, fake_token: str, fake_owm: OpenWeatherMap) -> None:
        assert fake_owm._token == fake_token
        assert fake_owm._BASE_URL == 'https://api.openweathermap.org/data/'
        assert fake_owm._VERSION == '2.5'
        assert fake_owm.units == 'metric'
        assert isinstance(fake_owm.flow_ctrl, RequestFlowController)

    def test__url(self, fake_owm: OpenWeatherMap) -> None:
        assert fake_owm._url == 'https://api.openweathermap.org/data/2.5/'

    def test__get(
        self,
        fake_owm: OpenWeatherMap,
        location_fake_data: dict[str, Any],
        monkeypatch: MonkeyPatch,
    ) -> None:
        class ResponsePatch:
            def raise_for_status(self) -> None:
                pass

            def json(self) -> None:
                return {'hello': 'world!'}

        fake_get: Mock = Mock(return_value=ResponsePatch())
        monkeypatch.setattr(requests, 'get', fake_get)
        params: dict[str, Any] = location_fake_data
        res: dict[str, Any] = fake_owm._get(
            url=fake_owm._url + 'weather', params=params
        )

        assert res == fake_get.return_value.json()

    def test_get_weather_by_coord(
        self,
        fake_owm: OpenWeatherMap,
        location_fake_data: dict[str, Any],
        monkeypatch: MonkeyPatch,
    ) -> None:
        fake_get: Mock = Mock(return_value={'weather': 'Good'})
        monkeypatch.setattr(OpenWeatherMap, '_get', fake_get)
        res: dict[str, Any] = fake_owm.get_weather_by_coord(
            **location_fake_data
        )

        assert res == fake_get.return_value

    def test_sub_map(self, fake_owm: OpenWeatherMap) -> None:
        assert len(list(fake_owm.sub_map(5))) == 2_592
