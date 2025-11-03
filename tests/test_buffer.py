import pytest

from src.helpers.buffer import Buffer
from src.helpers.text import Text


@pytest.fixture
def buffer():
    return Buffer()


def test_buffer_add(buffer):
    buffer.add(
        {"test": 2, "test2": Text(text="test", rot_type="rot13", status="encrypted")}
    )
    buffer.add(Text(text="test2", rot_type="rot47", status="decrypted"))

    assert len(buffer.data) == 2  # nosec B101


def test_buffer_get_all(buffer):
    assert buffer.get_all() == []  # nosec B101
    # bandit???


def test_buffer_is_cleared(buffer):
    buffer.data.clear()

    assert buffer.data == []  # nosec B101
