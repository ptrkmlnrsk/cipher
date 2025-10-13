import json
from typing import Any
from dataclasses import asdict


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> dict | None:
        try:
            with open(input_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found")

    @staticmethod
    def write_file(encrypted_data: Any, output_file_path: str) -> None:
        try:
            with open(output_file_path, "w") as file:
                json.dump(asdict(encrypted_data), file)
        except IOError:
            print("File not found")

    @staticmethod
    def append_to_file(encrypted_data: Any, file_path: str) -> None:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not found")

        data["result"].append(asdict(encrypted_data))

        try:
            with open(file_path, "w") as file:
                json.dump(data, file)
        except IOError:
            print("File has not been updated with new data")
