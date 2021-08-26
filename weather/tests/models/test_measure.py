from typing import Any
import pytest
from django.db.utils import IntegrityError
from django.db import transaction
from weather.models import Measure, Location, City, Country, Weather


class TestMeasure:
    def test_init(self, measure_fake_data: dict[str, Any]) -> None:
        measure: Measure = Measure(**measure_fake_data)

        for field, value in measure_fake_data.items():
            assert hasattr(measure, field)
            assert isinstance(getattr(measure, field), type(value))

    @pytest.mark.django_db
    def test_creation(
        self,
        measure_fake_data: dict[str, Any],
        location_fake_data: dict[str, Any],
        country_fake_data: dict[str, Any],
        city_fake_data: dict[str, Any],
        weather_fake_data: dict[str, Any],
    ) -> None:
        country: Country = Country.objects.create(**country_fake_data)
        city: City = City.objects.create(**city_fake_data, country=country)
        location: Location = Location.objects.create(
            **location_fake_data,
            city=city,
        )
        weather: Weather = Weather.objects.create(**weather_fake_data)
        measure: Measure = Measure.objects.create(
            **measure_fake_data, location=location, weather=weather
        )
        assert str(measure) == str(measure.measure_id)

        with pytest.raises(IntegrityError), transaction.atomic():
            Measure.objects.create(**measure_fake_data, location=location)

        with pytest.raises(IntegrityError), transaction.atomic():
            Measure.objects.create(**measure_fake_data, weather=weather)

        with pytest.raises(IntegrityError), transaction.atomic():
            Measure.objects.create(**measure_fake_data)

    @pytest.mark.django_db
    def test_next_measure_num(
        self,
        measure_fake_data: dict[str, Any],
        location_fake_data: dict[str, Any],
        country_fake_data: dict[str, Any],
        city_fake_data: dict[str, Any],
        weather_fake_data: dict[str, Any],
    ) -> None:
        assert Measure.objects.next_measure_num() == 1

        country: Country = Country.objects.create(**country_fake_data)
        city: City = City.objects.create(**city_fake_data, country=country)
        location: Location = Location.objects.create(
            **location_fake_data,
            city=city,
        )
        weather: Weather = Weather.objects.create(**weather_fake_data)
        Measure.objects.create(
            **measure_fake_data, location=location, weather=weather
        )

        assert Measure.objects.next_measure_num() == 2

    @pytest.mark.django_db
    def test_latest_measure_num(
        self,
        measure_fake_data: dict[str, Any],
        location_fake_data: dict[str, Any],
        country_fake_data: dict[str, Any],
        city_fake_data: dict[str, Any],
        weather_fake_data: dict[str, Any],
    ) -> None:
        assert Measure.objects.latest_measure_num() == None

        country: Country = Country.objects.create(**country_fake_data)
        city: City = City.objects.create(**city_fake_data, country=country)
        location: Location = Location.objects.create(
            **location_fake_data,
            city=city,
        )
        weather: Weather = Weather.objects.create(**weather_fake_data)
        Measure.objects.create(
            **measure_fake_data, location=location, weather=weather
        )

        assert Measure.objects.latest_measure_num() == 1
