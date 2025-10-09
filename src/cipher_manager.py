from cipher_properties import ROT13, ROT47
from file_handler import FileHandler
from buffer import Text
from typing import Any

from src import file_handler


class CipherManager:
    def __init__(self, file_handler: Any, rot13: Any, rot47: Any): # dependency injection z bufferem, file_handlere, ciperem
        self.file_handler = file_handler
        self.rot13 = rot13
        self.rot47 = rot47

    def read_file(self, file_path: str) -> dict:
        return self.file_handler.read_file(file_path)
#
    def encrypt(self, text_input: str, rot_type: str) -> Text:
        if rot_type == 'rot13':
            return self.rot13.encrypt_data(text_input)
        else:
            return self.rot47.encrypt_data(text_input)
#
#    def decrypt(self):
#        pass
#
#    def write_file(self, write_file: str, output_file_path: str):
#        pass
#    @staticmethod
#    def append_to_file(encrypted_data: str, file_path: str):
#        FileHandler.append_to_file(encrypted_data, file_path)
#
#    def exit_program(self):
#        pass

