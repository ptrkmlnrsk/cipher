import json
from typing import Any
from dataclasses import asdict
from buffer import Text

class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> dict[str, Any]:
        with open(input_file, "r") as file:
            return json.load(file)

    @staticmethod
    def write_file(encrypted_data: Any, output_file_path: str):
        with open(output_file_path, "w") as file:
            #file.write(encrypted_data)
            json.dump(asdict(encrypted_data), file)

    @staticmethod
    def append_to_file(encrypted_data: Any, file_path: str):
        with open(file_path, "r") as file:
            data = json.load(file)

        data['result'].append(asdict(encrypted_data))

        with open(file_path, "w") as file:
            json.dump(data, file) # inna struktura jsona
            # inaczej się dodaje do jsona, wczytać i zapisać