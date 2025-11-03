import pytest

from src.rots.rot13 import ROT13
from src.helpers.text import Text
from src.helpers.const import ROT13_TYPE, ENCRYPTED, DECRYPTED


@pytest.fixture
def t_rot13():
    return ROT13()


@pytest.mark.parametrize(
    "plain, encrypted",
    [("Patryk cos tam", "Cngelx pbf gnz"), ("abc", "nop"), ("ABC", "NOP")],
)
def test_cipher_rot13(t_rot13, plain, encrypted):
    assert t_rot13.cipher(shift=13, text=plain) == encrypted  # nosec B101


def test_encrypt_data(t_rot13):
    check = t_rot13.encrypt_data("Patryk cos tam")
    assert isinstance(check, Text)  # nosec B101
    assert check.text == "Cngelx pbf gnz"  # nosec B101
    assert check.rot_type == ROT13_TYPE  # nosec B101
    assert check.status == ENCRYPTED  # nosec B101


def test_decrypt_data(t_rot13):
    text_obj = Text(text="Cngelx pbf gnz", rot_type="rot13", status="encrypted")
    check = t_rot13.decrypt_data(text_obj)
    assert isinstance(check, Text)  # nosec B101
    assert check.text == "Patryk cos tam"  # nosec B101
    assert check.rot_type == ROT13_TYPE  # nosec B101
    assert check.status == DECRYPTED  # nosec B101
