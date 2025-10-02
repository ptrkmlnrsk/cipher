from cipher_properties import Rot13, CipherOutput
from encrypt_decrypt import EncryptDecrypt
from file_handler import FileHandler

def main():

    # tu powinna być fasada jako jedna klasa?

    file_handler = FileHandler()
    file_data = file_handler.read_file(input("Enter file path: "))
    rot13 = Rot13(CipherOutput(text=None, rot_type=None, status=None))
    print(rot13.encrypt_data(file_data))
    print(rot13.decrypt_data())


    #print("File contents:", cipher_data.text)

if __name__ == '__main__':
    main()