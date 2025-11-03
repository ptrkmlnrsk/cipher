import pytest
import json
import os

from src.handlers.file_handler import FileHandler
from src.helpers.text import Text


@pytest.fixture
def file_handler():
    return FileHandler()


def test_read_file(file_handler):
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(
            {"result": [{"text": "test2", "rot_type": "rot47", "status": "decrypted"}]},
            f,
        )

    tests_list = file_handler.read_file("test.json")

    assert isinstance(tests_list[0], Text)  # nosec B101
    assert tests_list[0] == Text(text="test2", rot_type="rot47", status="decrypted")  # nosec B101

    os.remove("test.json")


def test_write_file():
    test_data_to_save = [
        Text(text="grfg", rot_type="rot13", status="encrypted"),
        Text(text="E6DE", rot_type="rot47", status="encrypted"),
    ]
    FileHandler.write_file(test_data_to_save, "test.json")

    assert os.path.exists("test.json")  # nosec B101
    os.remove("test.json")


def test_append_to_file():
    with open("test.json", "w", encoding="utf-8") as f:
        json.dump(
            {"result": [{"text": "test2", "rot_type": "rot47", "status": "decrypted"}]},
            f,
        )
    test_data_to_append = Text(text="E6DE", rot_type="rot47", status="encrypted")
    FileHandler.append_to_file(test_data_to_append, "test.json")

    with open("test.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == {
        "result": [
            {"text": "test2", "rot_type": "rot47", "status": "decrypted"},
            {"text": "E6DE", "rot_type": "rot47", "status": "encrypted"},
        ]
    }  # nosec B101

    os.remove("test.json")
