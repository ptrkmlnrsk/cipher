from .buffer import Text
from .rot13 import ROT13
from .rot47 import ROT47
from .file_handler import FileHandler
from .const import ROT13_TYPE, ROT47_TYPE
from .buffer import Buffer


class Manager:
    def __init__(
        self,
        handler: FileHandler = FileHandler(),
        rot13: ROT13 = ROT13(),
        rot47: ROT47 = ROT47(),
        buffer: Buffer = Buffer(),
    ):
        self.file_handler = handler
        self.rot13 = rot13
        self.rot47 = rot47
        self.buffer = buffer

    def read_file(self, file_path: str) -> dict:
        return self.file_handler.read_file(file_path)

    def write_file(self, write_file: str, output_file_path: str) -> None:
        pass

    def append_to_file(self, encrypted_data: str, file_path: str) -> None:
        pass

    def encrypt(self, text_input: str, user_rot_type: str) -> Text:
        if user_rot_type == ROT13_TYPE:
            return self.rot13.encrypt_data(input_str=text_input)
        else:
            return self.rot47.encrypt_data(input_str=text_input)

    def decrypt(self):
        pass

    @staticmethod
    def show_options() -> None:
        print(
            "1 - Read file"
            "\n2 - Encrypt data"
            "\n3 - Decrypt data"
            "\n4 - Write file"
            "\n5 - Append to file"
            "\n6 - Show buffer"
            "\n7 - Clear buffer"
            "\n8 - Exit"
        )

    def menu(self, command: int) -> None:
        match command:
            case 1:  # read file
                try:
                    file_to_read = input("Enter file name: ")
                    input_file_path = f".\\files\\{file_to_read}.json"
                    file = self.file_handler.read_file(input_file=input_file_path)
                    self.buffer.add(file)
                    print("File loaded!")
                except FileNotFoundError:
                    print("File not found! Try again!")

            case 2:  # encrypt
                # 1 / 2
                user_rot = input("\nChose encryption mode: 1 - rot13\n 2 - rot47")
                if user_rot == "1":
                    user_input = str(input("Enter text to encrypt: "))
                    encrypted = self.encrypt(
                        text_input=user_input, user_rot_type=ROT13_TYPE
                    )
                    self.buffer.add(encrypted)
                elif user_rot == "2":
                    user_input = str(input("Enter text to encrypt: "))
                    encrypted = self.encrypt(
                        text_input=user_input, user_rot_type=ROT47_TYPE
                    )
                    self.buffer.add(encrypted)
                else:
                    print("You need to enter 1 or 2")

            case 3:  # decrypt
                pass

            case 4:  # write file
                user_input_file_name = input("\nEnter file name: ")
                output_file_path = f".\\files\\{user_input_file_name}.json"
                if self.buffer.is_empty() is not True:
                    try:
                        self.file_handler.write_file(self.buffer.data, output_file_path)
                    except IOError:
                        print("Error occurred while writing file")
                else:
                    print(
                        "File not written. You need to add some data to properly save file"
                    )

            case 5:  # append to file
                output_file_name = input("\nEnter file name: ")
                output_file_path = f".\\files\\{output_file_name}.json"
                try:
                    buffer_out = self.buffer.get_all()
                    for text_obj in buffer_out:
                        if isinstance(text_obj, Text):
                            self.file_handler.append_to_file(text_obj, output_file_path)
                except IOError:
                    print(
                        "Some problem occurred while appending to file. Might be wrong filepath. Try again!"
                    )

            case 6:  # show buffer data
                print(self.buffer.data)

            case 7:  # clear buffer
                self.buffer.clear()
                print("Buffer cleared! You can add new data to buffer.")

            # TODO handling bufora jeśli jest tam wczytana treść pliku json
