import pytest

from src.rots.rot47 import ROT47
from src.helpers.text import Text
from src.helpers.const import ROT47_TYPE, ENCRYPTED, DECRYPTED


@pytest.fixture
def rot_47():
    return ROT47()


@pytest.mark.parametrize(
    "plain, encrypted",
    [("Lubie placki", "{F3:6 A=24<:"), ("abc", "234"), ("ABC", "pqr")],
)
def test_cipher_rot13(rot_47, plain, encrypted):
    assert rot_47.cipher(shift=47, text=plain) == encrypted  # nosec B101


def test_encrypt_data(rot_47):
    check = rot_47.encrypt_data("Lubie placki")
    assert isinstance(check, Text)  # nosec B101
    assert check.text == "{F3:6 A=24<:"  # nosec B101
    assert check.rot_type == ROT47_TYPE  # nosec B101
    assert check.status == ENCRYPTED  # nosec B101


def test_decrypt_data(rot_47):
    text_obj = Text(text="{F3:6 A=24<:", rot_type="rot47", status="encrypted")
    check = rot_47.decrypt_data(text_obj)
    assert isinstance(check, Text)  # nosec B101
    assert check.text == "Lubie placki"  # nosec B101
    assert check.rot_type == ROT47_TYPE  # nosec B101
    assert check.status == DECRYPTED  # nosec B101
