import pytest

from demo_service.pricing import format_price
from demo_service.settings import currency


def test_prices_default_to_usd():
    assert format_price(1999) == "19.99 USD"


@pytest.mark.parametrize("code", ["EUR", "GBP"])
def test_prices_use_the_configured_currency(monkeypatch, code):
    monkeypatch.setenv("DEMO_CURRENCY", code)
    currency.cache_clear()  # the setting is cached, so read it again
    assert format_price(1999) == f"19.99 {code}"
