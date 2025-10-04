import json
from typing import Any
from dataclasses import asdict

class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> str:
        with open(input_file, "r") as file:
            return file.read()

    @staticmethod
    def write_file(encrypted_data: Any, output_file_path: str):
        with open(output_file_path, "w") as file:
            #file.write(encrypted_data)
            json.dump(asdict(encrypted_data), file)

    @staticmethod
    def append_to_file(encrypted_data: Any, file_path: str):
        with open(file_path, "a") as file:
            json.dump(asdict(encrypted_data), file)