"""Settings read from the environment."""

import functools
import os


@functools.cache
def currency() -> str:
    """The currency prices are shown in: DEMO_CURRENCY, or USD. Read once, then cached."""
    return os.environ.get("DEMO_CURRENCY", "USD")
