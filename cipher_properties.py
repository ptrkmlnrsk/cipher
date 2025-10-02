from cipher_abc import CipherMethods, CipherOutput
from typing import Any
import string

class Rot13(CipherMethods):
    def __init__(self, obj: CipherOutput):
        self.obj = obj

    def encrypt_data(self, text_to_encrypt: str) -> Any: # DataClass ROT13/ROT47:

        encrypted = []
        for char in text_to_encrypt:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + 13) % 26 + base)
                encrypted.append(new_char)
            else:
                encrypted.append(char)

        self.obj.text = text_to_encrypt
        self.obj.rot_type = 'rot13'
        self.obj.status = 'encrypted'

        return ''.join(encrypted)


    def decrypt_data(self) -> Any: # cipher object or only text

        if self.obj.status == 'encrypted':
            decrypted = []
            for char in self.obj.text:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    new_char = chr((ord(char) - base + 13) % 26 + base)
                    decrypted.append(new_char)
                else:
                    decrypted.append(char)

            self.obj.status = 'decrypted'
            return ''.join(decrypted)
        else:
            raise Exception('Data is not encrypted')





