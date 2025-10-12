from cipher_manager import CipherManager
from buffer import Buffer, Text
from file_handler import FileHandler
from cipher_properties import ROT13, ROT47
from typing import Any

def menu(command: str, buffer: Any, cipher_manager: Any) -> None:
    match command:
        case 'read file' | 'read':
            file = cipher_manager.read_file(file_path="D:\\repos\\cipher\\test_cipher.json")
            try:
                for existing_text in file['result']:
                    buffer.add(Text(text=existing_text['text'],
                                       rot_type=existing_text['rot_type'],
                                       status=existing_text['status']
                                       ))
            except KeyError:
                print('File is empty')
        case 'encrypt' | 'encrypt data':
            user_input = str(input("Enter text to encrypt: "))
            print('Chose encryption mode: rot13 or rot47')
            user_rot = input('Enter rotation mode: ')
            encrypted = cipher_manager.encrypt(text_input=user_input, rot_type=user_rot)
            buffer.add(encrypted)
        case 'decrypt' | 'decrypt data':
            pass
        case 'append' | 'append to file':
            output_file_path = r"D:\repos\cipher\test_cipher.json"
            buffer_out = buffer.get_all()
            for text_obj in buffer_out:
                    # handle not Text obj
                    cipher_manager.file_handler.append_to_file(text_obj, output_file_path)
            # TODO handling bufora jeśli jest tam wczytana treść pliku json

        case 'buffer':
            print(buffer.data)
        case 'quit':
            print("Program shut down")

def main():

    buffer = Buffer()
    file_handler = FileHandler()
    rot13 = ROT13()
    rot47 = ROT47()
    cipher_manager = CipherManager(handler=file_handler,
                                   rot13=rot13,
                                   rot47=rot47)

    while True:
        command = input("$ ")
        menu(command, buffer, cipher_manager)
        if command == 'quit':
            break


if __name__ == "__main__":
    main()