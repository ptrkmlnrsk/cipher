from file_handler import FileHandler


class CipherManager:
    def __init__(self): # dependency injection z bufferem, file_handlere, ciperem
        pass  

    def read_file(self, read_file: str) -> dict[str, Any]:
        pass

    def encrypt(self, encrypted_text: str) -> dict[str, Any]:
        pass

    def decrypt(self):
        pass

    def write_file(self, write_file: str, output_file_path: str):
        pass

    def append_to_file(self, append_to_file: str, file_path: str):
        pass

    def exit_program(self):
        pass

