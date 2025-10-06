from file_handler import FileHandler
from buffer import Buffer
from cipher_properties import ROT13


buffer = Buffer()
file_handler = FileHandler()
rot13 = ROT13()

def menu(command: str) -> None:
    while True:
        match command:
            case 'read file' | 'read':
                file = FileHandler.read_file(input(r"D:\repos\cipher\test_cipher.json"))
                #buffer.add(file)
            case 'encrypt' | 'encrypt data':
                user_input = input("Enter text to encrypt: ")
                encrypted = rot13.encrypt_data(input_str=user_input)
            case 'append' | 'append to file':
                output_file_path = r"D:\repos\cipher\test_cipher.json"
                file_handler.append_to_file(encrypted, output_file_path)
            case 'quit' | 'exit':
                print("Program shut down")
                break



def main():
    menu("menu")
if __name__ == "__main__":
    main()