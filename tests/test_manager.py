import os
import pytest
import json

from unittest.mock import Mock
from managers.manager import Manager
from helpers.text import Text
from unittest.mock import patch


@pytest.fixture
def manager():
    return Manager()


def show_message(msg):
    print(f"Tested message: {msg}")


def test_handle_read_file(manager):
    with open("test.json", "w", encoding="utf-8") as file:
        json.dump(
            {"result": [{"text": "test2", "rot_type": "rot47", "status": "decrypted"}]},
            file,
        )
    manager.base_dir = os.getcwd()
    manager.handle_read_file(user_read_file="test")

    assert len(manager.buffer.data) == 1

    os.remove("test.json")


@pytest.mark.parametrize(
    "to_encrypt, encryption_result", [("Patryk cos tam", "Cngelx pbf gnz"), ("", "")]
)
def test_encrypt_rot13(manager, to_encrypt, encryption_result):
    manager.encrypt(encryption_choice=1, text_to_encrypt=to_encrypt)
    assert manager.buffer.data[0].text == encryption_result


@pytest.mark.parametrize(
    "to_encrypt, encryption_result", [("Lubie placki", "{F3:6 A=24<:"), ("", "")]
)
def test_encrypt_rot47(manager, to_encrypt, encryption_result):
    manager.encrypt(encryption_choice=2, text_to_encrypt=to_encrypt)
    assert manager.buffer.data[0].text == encryption_result


def test_printing_encrypt_to_enter_proper_number_corresponding_with_type_of_cipher(
    manager,
):
    with patch("builtins.print") as mock_print:
        manager.encrypt(encryption_choice=3, text_to_encrypt="test")

    mock_print.assert_called_with("You need to enter 1 or 2!")


@pytest.mark.parametrize(
    "to_decrypt, rot_type, encryption_result",
    [("Cngelx pbf gnz", "rot13", "Patryk cos tam"), ("", "rot13", "")],
)
def test_decrypt_rot13(manager, to_decrypt, rot_type, encryption_result):
    manager.buffer.add([Text(text=to_decrypt, rot_type=rot_type, status="encrypted")])
    manager.decrypt()
    assert manager.buffer.data[1].text == encryption_result


@pytest.mark.parametrize(
    "to_decrypt, rot_type, encryption_result",
    [
        ("{F3:6 A=24<:", "rot47", "Lubie placki"),
        ("", "rot47", ""),
    ],
)
def test_decrypt_rot47(manager, to_decrypt, rot_type, encryption_result):
    manager.buffer.add([Text(text=to_decrypt, rot_type=rot_type, status="encrypted")])
    manager.decrypt()
    assert manager.buffer.data[1].text == encryption_result


@patch("builtins.print")
def test_handle_write_file_but_with_empty_buffer(mock_print, manager):
    manager.handle_write_file("test")
    mock_print.assert_called_with(
        "File not written. You need to add some data to properly save file"
    )


@patch("builtins.print")
def test_handle_write_file_with_unknow_error(mock_print, manager):
    manager.buffer.data = [Text(text="grfg", rot_type="rot13", status="encrypted")]
    manager.handle_write_file("test/")
    mock_print.assert_called_once_with("Error occurred while writing file")


def test_handle_append_to_file(manager):
    file_handler_mock = Mock()
    mock_buffer = Mock()
    mock_buffer.get_all.return_value = [
        Text(text="grfg", rot_type="rot13", status="encrypted")
    ]

    manager = Manager(handler=file_handler_mock, buffer=mock_buffer)

    manager.handle_append_to_file(file_to_append_to="test")

    file_handler_mock.append_to_file.assert_called_once()


def test_handle_append_to_file_raise_error(manager):
    file_handler_mock = Mock()
    file_handler_mock.append_to_file.side_effect = IOError()
    mock_buffer = Mock()
    mock_buffer.get_all.return_value = [
        Text(text="grfg", rot_type="rot13", status="encrypted")
    ]

    manager = Manager(handler=file_handler_mock, buffer=mock_buffer)
    with pytest.raises(IOError):
        manager.handle_append_to_file(file_to_append_to="test")

    file_handler_mock.append_to_file.assert_called_once()
