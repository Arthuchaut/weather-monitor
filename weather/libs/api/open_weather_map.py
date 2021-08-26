from typing import Any, Iterator
import pathlib
import time
import requests
from django.conf import settings
from weather.libs.api.request_flow_controller import RequestFlowController


class OpenWeatherMap:
    _BASE_URL: str = 'https://api.openweathermap.org/data/'
    _VERSION: str = '2.5'

    def __init__(self, token: str, calls_per_min: int) -> None:
        '''Constructor'''

        self._token: str = token
        self.units: str = 'metric'
        self.flow_ctrl: RequestFlowController = RequestFlowController(
            flow_capacity=calls_per_min,
            time_range=60,
            state_file=settings.BASE_DIR / '.flowstate',
        )

    @property
    def _url(self) -> str:
        '''Returns the formated URL.

        Returns:
            str: The formated URL.
        '''

        return self._BASE_URL + self._VERSION + '/'

    def sub_map(self, node_size: int) -> Iterator[list[tuple[float, float]]]:
        '''Subdivide the world map in a grid and generate
        a [lat, lon] coord for each node.

        Args:
            node_size (int): The size (in degree) for each node.

        Returns:
            Iterator[list[tuple[float, float]]]: The generated coord.
        '''

        for lat in range(90, -90, -node_size):
            for lon in range(-180, 180, node_size):
                center_lat = lat - (node_size / 2)
                center_lon = lon + (node_size / 2)

                yield center_lat, center_lon

    def _get(self, url: str, params: dict[str, Any] = {}) -> dict[str, Any]:
        '''Get the resource from the given URL and parameters.

        Args:
            url (str): The resource to access.
            params (Optional, dict[str, Any]): The query parameters.
                Default to {}.

        Raises:
            RequestError: If any exception is raised during the request.
                A maximum of 5 tries is permitted before raise the exception.

        Returns:
            dict[str, Any]: The API response in JSON format.
        '''

        tries: int = 5
        params.update(
            {
                'appid': self._token,
                'units': self.units,
            }
        )

        while tries:
            try:
                self.flow_ctrl.wait_for_free_flow()
                res: requests.Response = requests.get(url, params=params)
                res.raise_for_status()
                break
            except Exception as e:
                tries -= 1

                if not tries:
                    raise RequestError(e)

                time.sleep(1)

        return res.json()

    def get_weather_by_coord(self, lat: float, lon: float) -> dict[str, Any]:
        '''Retrieve the current weather data from the lat/lon coord.

        Args:
            lat (float): The latitude.
            lon (float): The longitude.

        Returns:
            dict[str, Any]: The current weather in JSON format.
        '''

        url: str = self._url + 'weather'
        params: dict[str, Any] = {'lat': lat, 'lon': lon}
        return self._get(url, params=params)


class RequestError(Exception):
    ...
