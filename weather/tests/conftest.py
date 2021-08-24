from typing import Any
import pytest


@pytest.fixture
def country_fake_data() -> dict[str, Any]:
    return {
        'name': 'France',
        'country_code': 'FR',
    }
