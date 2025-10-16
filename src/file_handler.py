import json
from typing import Any
from dataclasses import asdict


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> dict | None:
        with open(input_file, "r") as file:
            return json.load(file)
            # TODO check if file is empty

    @staticmethod
    def write_file(encrypted_data: Any, output_file_path: str) -> None:
        with open(output_file_path, "w") as file:
            # TODO TypeError: asdict() should be called on dataclass instances
            empty_l = []
            result = {"result": empty_l}
            for text_obj in encrypted_data:
                empty_l.append(asdict(text_obj))
            json.dump(result, file)

    @staticmethod
    def append_to_file(encrypted_data: Any, file_path: str) -> None:
        with open(file_path, "r") as file:
            data = json.load(file)
            data["result"].append(asdict(encrypted_data))

        with open(file_path, "w") as file:
            json.dump(data, file)
