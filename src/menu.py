from src.file_handler import FileHandler
from src.buffer import Buffer
from cipher_properties import ROT13


buffer = Buffer()
file_handler = FileHandler()
rot13 = ROT13()

def menu(command: str) -> None:
    match command:
        case 'read file' | 'read':
            file = FileHandler.read_file("D:\\repos\\cipher\\test_cipher2.json")
            buffer.add(file)
        case 'encrypt' | 'encrypt data':
            user_input = input("Enter text to encrypt: ")
            encrypted = rot13.encrypt_data(input_str=user_input)
            buffer.add(encrypted)
        case 'append' | 'append to file':
            output_file_path = r"D:\repos\cipher\test_cipher.json"
            user_input = input("Enter text to encrypt: ")
            encrypted = rot13.encrypt_data(input_str=user_input)
            buffer.add(encrypted)
            file_handler.append_to_file(encrypted, output_file_path)
        case 'quit':
            print("Program shut down")

def main():
    while True:
        command = input("$ ")
        menu(command)
        if command == 'quit':
            break


if __name__ == "__main__":
    main()