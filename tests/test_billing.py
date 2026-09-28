from datetime import UTC, datetime

from demo_service.billing import invoice_date


def test_invoice_is_dated_in_utc():
    before = datetime.now(UTC).date()
    dated = invoice_date()
    after = datetime.now(UTC).date()
    assert dated in {before, after}
