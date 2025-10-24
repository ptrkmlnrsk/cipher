from src.managers.manager import Manager


class Menu:
    def __init__(self):
        self.manager = Manager()

    @staticmethod
    def _prompt_nonempty(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value == "":
                print("Please enter a none empty string")
            else:
                return value

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

    def menu_handler(self, command: int) -> None:
        match command:
            case 1:
                input_to_read = str(input("Enter file name: "))
                self.manager.handle_read_file(input_to_read)
            case 2:
                user_encryption_choice = int(
                    input("Enter encryption type - 1 (rot13) or 2 (rot47): ")
                )
                user_text_to_encrypt = self._prompt_nonempty("Enter text: ")
                self.manager.encrypt(user_encryption_choice, user_text_to_encrypt)
            case 3:
                self.manager.decrypt()
            case 4:
                user_output_filename = self._prompt_nonempty("Enter output filename: ")
                self.manager.handle_write_file(user_output_filename)
            case 5:
                input_file_to_append_to = self._prompt_nonempty(
                    "Enter filename to append to: "
                )
                self.manager.handle_append_to_file(input_file_to_append_to)
            case 6:
                print(self.manager.buffer.data)
            case 7:
                self.manager.buffer.clear()
                print("Buffer cleared! You can add new data to buffer.")
