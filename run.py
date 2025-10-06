from src.cipher_properties import ROT13
from file_handler import FileHandler


def main():

    # tu powinna być fasada jako jedna klasa?
    # zdefiniowac zeby ktos wpisl tu lub tu jakas litere i w zaleznosci od tego robi rota

    file_handler = FileHandler()
    encrypt_decrypt = ROT13()

    encrypted_file = file_handler.read_file(r"D:\repos\cipher\test_cipher.json")

    print("Encrypted file: ", encrypted_file)
    for encrypted_line in encrypted_file['result']:


    #encrypted = encrypt_decrypt.decrypt_data(encrypted_file)

    #encrypt_decrypt.decrypt_data(encrypted)
    #print(encrypted.text)

    #file_handler.append_to_file(encrypted, 'test_cipher.json')



if __name__ == '__main__':
    main()