import pytest

from demo_service import registry


@pytest.fixture(autouse=True)
def _reset_registry():
    registry._users.clear()
    yield
    registry._users.clear()
