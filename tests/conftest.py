import pytest

from demo_service.settings import currency


@pytest.fixture(autouse=True)
def _reset_currency_cache():
    """Clear the cached currency setting before and after each test so no test sees another's value."""
    currency.cache_clear()
    yield
    currency.cache_clear()
