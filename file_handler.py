import json

class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def read_file(input_file: str) -> str:
        with open(input_file, "r") as file:
            return file.read()

    @staticmethod
    def write_file(encrypted_data: str, output_file_path: str):
        with open(output_file_path, "w") as file:
            #file.write(encrypted_data)
            json.dump(encrypted_data, file)

    @staticmethod
    def append_to_file(encrypted_data: str, output_file_path: str):
        with open(encrypted_data, "a") as file:
            file.write(output_file_path)