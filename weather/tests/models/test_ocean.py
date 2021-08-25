from typing import Any
import pytest
from weather.models import Ocean


class TestOcean:
    def test_init(self, ocean_fake_data: dict[str, Any]) -> None:
        ocean: Ocean = Ocean(**ocean_fake_data)

        for field, value in ocean_fake_data.items():
            assert hasattr(ocean, field)
            assert isinstance(getattr(ocean, field), type(value))

    @pytest.mark.django_db
    def test_creation(self, ocean_fake_data: dict[str, Any]) -> None:
        ocean: Ocean = Ocean.objects.create(**ocean_fake_data)
        assert str(ocean) == ocean_fake_data['name']
