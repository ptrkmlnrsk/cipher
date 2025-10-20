from .buffer import Text
from .rot13 import ROT13
from .rot47 import ROT47
from .file_handler import FileHandler
from .const import ROT13_TYPE, ROT47_TYPE, ENCRYPTED
from .buffer import Buffer


class Manager:
    def __init__(
        self,
        handler: FileHandler = FileHandler(),
        rot13: ROT13 = ROT13(),
        rot47: ROT47 = ROT47(),
        buffer: Buffer = Buffer(),
        base_dir: str = "",
    ):
        self.file_handler = handler
        self.rot13 = rot13
        self.rot47 = rot47
        self.buffer = buffer
        self.base_dir = base_dir

    def _handle_read_file(self, user_read_file: str) -> None:
        file = self.file_handler.read_file(
            input_file=f"{self.base_dir}/{user_read_file}.json"
        )
        self.buffer.add(file)

    def _encrypt(self, encryption_choice: int, text_to_encrypt: str) -> None:
        if encryption_choice == 1:
            encrypted = self.rot13.encrypt_data(input_str=text_to_encrypt)

            self.buffer.add(encrypted)
        elif encryption_choice == 2:
            encrypted = self.rot47.encrypt_data(input_str=text_to_encrypt)

            self.buffer.add(encrypted)
        else:
            print("You need to enter 1 or 2")

    def _decrypt(self) -> None:
        if not self.buffer.data:
            print("No data to encrypt!")
        else:
            for obj in self.buffer.data:
                try:
                    if obj.status == ENCRYPTED:
                        if obj.rot_type == ROT13_TYPE:
                            self.buffer.data.append(self.rot13.decrypt_data(obj))
                        elif obj.rot_type == ROT47_TYPE:
                            self.buffer.data.append(self.rot47.decrypt_data(obj))
                except AttributeError:
                    print("Encryption failed")

    def _handle_write_file(self, output_filename: str) -> None:
        if not self.buffer.data:
            print("File not written. You need to add some data to properly save file")
        else:
            try:
                self.file_handler.write_file(
                    self.buffer.data,
                    output_file_path=f"{self.base_dir}/{output_filename}.json",
                )
            except IOError:
                print("Error occurred while writing file")

    def _handle_append_to_file(self, file_to_append_to: str) -> None:
        try:
            buffer_out = self.buffer.get_all()
            for text_obj in buffer_out:
                if isinstance(text_obj, Text):
                    self.file_handler.append_to_file(
                        text_obj, file_path=f"{self.base_dir}/{file_to_append_to}.json"
                    )
        except IOError:
            print(
                "Some problem occurred while appending to file. Might be wrong filepath. Try again!"
            )

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
            case 1:
                input_to_read = input("Enter file name: ")
                self._handle_read_file(input_to_read)
            case 2:
                user_encryption_choice = int(input("Enter encryption type - 1 or 2: "))
                user_text_to_encrypt = input("Enter text: ")
                self._encrypt(user_encryption_choice, user_text_to_encrypt)
            case 3:
                self._decrypt()
            case 4:
                user_output_filename = input("Enter output file name: ")
                self._handle_write_file(user_output_filename)
            case 5:
                input_file_to_append_to = input("Enter file name: ")
                self._handle_append_to_file(input_file_to_append_to)
            case 6:
                print(self.buffer.data)
            case 7:
                self.buffer.clear()
                print("Buffer cleared! You can add new data to buffer.")
