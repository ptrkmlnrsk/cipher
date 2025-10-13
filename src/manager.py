from buffer import Text
from typing import Any
from rot13 import ROT13
from rot47 import ROT47
from file_handler import FileHandler


class Manager:
    def __init__(
        self,
        handler: FileHandler = FileHandler,
        rot13: ROT13 = ROT13,
        rot47: ROT47 = ROT47,
    ):
        self.file_handler = handler
        self.rot13 = rot13
        self.rot47 = rot47

    def read_file(self, file_path: str) -> dict:
        return self.file_handler.read_file(file_path)

    def write_file(self, write_file: str, output_file_path: str):
        pass

    @staticmethod
    def append_to_file(encrypted_data: str, file_path: str):
        pass

    def encrypt(self, text_input: str, user_rot_type: str) -> Text:
        if (
            user_rot_type == self.rot13
        ):  # dość sztywne wpisanie rot'a # ROTS = [ROT13, ROT47], ROT13 = 'rot13'
            return self.rot13.encrypt_data(text_input)
        else:
            return self.rot47.encrypt_data(text_input)

    def decrypt(self):
        pass

    def exit_program(self):
        pass


class CommandCenter(Manager):
    def show_options(self) -> None:
        pass

    def get_choice(self) -> None:
        pass

    def menu(self, command: str, buffer: Any, cipher_manager: Any) -> None:
        match command:
            case "encrypt" | "encrypt data":
                user_input = str(input("Enter text to encrypt: "))
                print("Chose encryption mode: rot13 or rot47")  # 1 / 2
                user_rot = input("Enter rotation mode: rot13 or rot47")
                encrypted = self.encrypt(text_input=user_input, user_rot_type=user_rot)
                buffer.add(encrypted)

            case "decrypt" | "decrypt data":
                pass

            case "read file" | "read":
                file = cipher_manager.read_file(file_path="/files/test_cipher.json")
                # TODO file - scieżka wzgledna i do stałej
                try:
                    for existing_text in file["result"]:
                        buffer.add(Text(**existing_text))
                except KeyError:
                    print("File is empty")

            case "append" | "append to file":
                output_file_path = r"/files/test_cipher.json"
                buffer_out = buffer.get_all()
                for text_obj in buffer_out:
                    # handle not Text obj
                    self.file_handler.append_to_file(text_obj, output_file_path)
                # TODO handling bufora jeśli jest tam wczytana treść pliku json

            case "buffer":
                print(buffer.data)

            case "quit":
                print("Program shut down")

    def show_buffer(self) -> None:
        pass
