import json
from typing import Any
from dataclasses import asdict

from src.helpers.text import Text


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> list[Text] | None:
        try:
            with open(input_file, "r", encoding="utf-8") as file:
                data = json.load(file)

                if not data or "result" not in data or not data["result"]:
                    return []

                return [Text(**text) for text in data["result"]]
        except FileNotFoundError:
            print(f"File {input_file} not found.")
            return []
        except json.decoder.JSONDecodeError:
            print(f"File {input_file} not a valid JSON file.")
            return []

    @staticmethod
    def write_file(encrypted_data: Any, output_file_path: str) -> None:
        result = {"result": [asdict(text_obj) for text_obj in encrypted_data]}
        with open(output_file_path, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=2)

    @staticmethod
    def append_to_file(encrypted_data: Any, file_path: str) -> None:
        with open(file_path, "r") as file:
            data = json.load(file)

        data["result"] += [asdict(text_obj) for text_obj in encrypted_data]
        # TODO dorobić funkcje pomocniczą w bufferze

        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)
