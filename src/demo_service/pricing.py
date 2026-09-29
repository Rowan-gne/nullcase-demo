"""Price formatting."""

from demo_service.settings import currency


def format_price(cents: int) -> str:
    """Format a price given in cents, e.g. 1999 -> "19.99 USD"."""
    return f"{cents / 100:.2f} {currency()}"
