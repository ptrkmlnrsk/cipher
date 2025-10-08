from cipher_properties import ROT13, ROT47
from file_handler import FileHandler
from buffer import Buffer


class CipherManager:
    def __init__(self, file_handler: FileHandler, rot13: ROT13, rot47: ROT47, buffer: Buffer): # dependency injection z bufferem, file_handlere, ciperem
        self.file_handler = file_handler
        self.rot13 = rot13
        self.rot47 = rot47
        self.buffer = buffer

#    def read_file(self, file_path: str) -> dict[str, Any]:
#        pass
#
#    def encrypt(self, encrypted_text: str) -> dict[str, Any]:
#        pass
#
#    def decrypt(self):
#        pass
#
#    def write_file(self, write_file: str, output_file_path: str):
#        pass
#
#    def append_to_file(self, append_to_file: str, file_path: str):
#        pass
#
#    def exit_program(self):
#        pass

