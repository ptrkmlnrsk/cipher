from cipher_properties import CipherData
from encrypt_decrypt import EncryptDecrypt
from file_handler import FileHandler

def main():

    # tu powinna być fasada jako jedna klasa?

    file_handler = FileHandler()
    file_data = file_handler.read_file(input("Enter file path: "))
    cipher_data = CipherData(file_data, "ROT13", "encrypt")
    print("File contents:", cipher_data.text)

if __name__ == '__main__':
    main()