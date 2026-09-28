import sys
from datetime import UTC, date, datetime

import pytest

from demo_service.billing import invoice_date


class _UTCDate(date):
    """date whose today() is the current UTC calendar date, matching billing's contract."""

    @classmethod
    def today(cls):
        return datetime.now(UTC).date()


@pytest.fixture(autouse=True)
def _utc_today(monkeypatch):
    monkeypatch.setattr(sys.modules[__name__], "date", _UTCDate)


def test_invoice_is_dated_today():
    assert invoice_date() == date.today()
