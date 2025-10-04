from cipher_properties import CaesarRots, CipherOutput
from file_handler import FileHandler
from cipher_core import rot13_core
from dataclasses import asdict

def main():

    # tu powinna być fasada jako jedna klasa?
    # zdefiniowac zeby ktos wpisl tu lub tu jakas litere i w zaleznosci od tego robi rota

    file_handler = FileHandler()
    #file_data = file_handler.read_file(input("Enter file path: "))
    file_data = file_handler.read_file('D:\\repos\\dump\\cipher\\test_cipher.txt')
    encrypt_decrypt = CaesarRots()

    encrypted = encrypt_decrypt.encrypt_data(input_str=file_data)
    print(encrypted.text)
    file_handler.write_file(encrypted, input("Output file path with extension: "))

    encrypt_decrypt.decrypt_data(encrypted)
    print(encrypted.text)

    file_handler.append_to_file(encrypted, input("Append to file: "))



if __name__ == '__main__':
    main()