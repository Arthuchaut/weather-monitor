from typing import Any
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.core.management.base import BaseCommand
from weather.libs.api.open_weather_map import OpenWeatherMap
from weather.models import Measure, Location, City, Country, Weather, Ocean


class Command(BaseCommand):
    '''The data collector command class.
    Allow to retrieve the current weather in the entier world.
    '''

    help: str = (
        'Retrieve the current weather '
        'in the entier world and save these data in DB.'
    )

    def handle(self, *args: Any, **kwargs: Any) -> None:
        '''Execute the command.
        - Split the world map into a list of [lat, lon] coords;
        - For each coord, collect the current weather;
        - Save each data in DB.

        Args:
            *args (Any): A list of variable parameters.
            **kwargs (Any): A dict of named parameters.
        '''

        measure_num: int = Measure.objects.next_measure_num()
        owm: OpenWeatherMap = OpenWeatherMap(
            token=settings.APP_CONFIG.OWM_APPID,
            calls_per_min=settings.APP_CONFIG.OWM_CALLS_PER_MIN,
        )
        i: int = 0

        for lat, lon in owm.sub_map(settings.APP_CONFIG.OWM_NODE_SIZE):
            data: dict[str, Any] = owm.get_weather_by_coord(lat=lat, lon=lon)

            if country_code := data['sys'].get('country'):
                country: Country = Country.objects.get(
                    country_code=country_code
                )
                city, _ = City.objects.get_or_create(
                    city_id=data['id'], name=data['name'], country=country
                )
                location, _ = Location.objects.get_or_create(
                    lat=lat, lon=lon, city=city
                )
            else:
                ocean, _ = Ocean.objects.get_or_create(name='Unknown Ocean')
                location, _ = Location.objects.get_or_create(
                    lat=lat, lon=lon, ocean=ocean
                )

            weather, _ = Weather.objects.get_or_create(
                weather_id=data['weather'][0]['id'],
                state=data['weather'][0]['main'],
                description=data['weather'][0]['description'],
            )
            measure: Measure = Measure.objects.create(
                measure_num=measure_num,
                measured_at=datetime.fromtimestamp(
                    data['dt'], tz=timezone.utc
                ),
                tz_timestamp=data['timezone'],
                wind_speed=data['wind']['speed'],
                wind_deg=data['wind']['deg'],
                wind_gust=data['wind'].get('gust'),
                visibility=data['visibility'],
                temp=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                temp_min=data['main']['temp_min'],
                temp_max=data['main']['temp_max'],
                pressure=data['main']['pressure'],
                humidity=data['main']['humidity'],
                sea_level=data['main'].get('sea_level'),
                ground_level=data['main'].get('grnd_level'),
                weather=weather,
                location=location,
            )

            if not i % 100:
                self.stdout.write(
                    f'{datetime.now():%Y-%m-%d %H:%M:%S} > Collected {i} weather data.'
                )

            i += 1

        self.stdout.write(
            f'{datetime.now():%Y-%m-%d %H:%M:%S} > Collected {i} weather data.'
        )
