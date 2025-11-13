from src.rots.rot13 import ROT13
from src.rots.rot47 import ROT47
from src.handlers.file_handler import FileHandler
from src.helpers.const import ROT13_TYPE, ROT47_TYPE, ENCRYPTED, BASE_DIR
from src.helpers.buffer import Buffer


class Manager:
    def __init__(
        self,
        handler: FileHandler = None,
        rot13: ROT13 = None,
        rot47: ROT47 = None,
        buffer: Buffer = None,
        base_dir: str = BASE_DIR,
    ):
        self.file_handler = handler or FileHandler()
        self.rot13 = rot13 or ROT13()
        self.rot47 = rot47 or ROT47()
        self.buffer = buffer or Buffer()
        self.base_dir = base_dir

    def handle_read_file(self, user_read_file: str) -> None:
        file = self.file_handler.read_file(
            input_file=f"{self.base_dir}/{user_read_file}.json"
        )
        self.buffer.add(file)

    def encrypt(self, encryption_choice: int, text_to_encrypt: str) -> None:
        if encryption_choice == 1:
            encrypted = self.rot13.encrypt_data(input_str=text_to_encrypt)

            self.buffer.add(encrypted)
        elif encryption_choice == 2:
            encrypted = self.rot47.encrypt_data(input_str=text_to_encrypt)

            self.buffer.add(encrypted)
        # else:
        #     print("You need to enter 1 or 2!")

    def decrypt(self) -> None:
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

    def handle_write_file(self, output_filename: str) -> None:
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

    def handle_append_to_file(self, file_to_append_to: str) -> None:
        try:
            buffer_out = self.buffer.get_all()
            # TODO przez te pętle plik jest otwierany kilka razy. Zmienić to i dodać po prostu do pliku
            self.file_handler.append_to_file(
                buffer_out, file_path=f"{self.base_dir}/{file_to_append_to}.json"
            )
        except IOError as e:
            raise IOError(
                "Some problem occurred while appending to file. Might be wrong filepath. Try again!"
            ) from e
