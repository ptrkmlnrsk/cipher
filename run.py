from cipher_properties import CaesarRots, CipherOutput
from file_handler import FileHandler
from cipher_core import rot13_core

def main():

    # tu powinna być fasada jako jedna klasa?

    file_handler = FileHandler()
    file_data = file_handler.read_file(input("Enter file path: "))
    #rot13 = CaesarRots(CipherOutput(text=None, rot_type=None, status=None))
    #print(rot13.encrypt_data(file_data))
    #print(rot13.decrypt_data())
    rot47 = CaesarRots(CipherOutput(text=None, rot_type=None, status=None))
    print(rot47.encrypt_data(file_data))
    print(rot47.decrypt_data())



    #print("File contents:", cipher_data.text)

if __name__ == '__main__':
    main()