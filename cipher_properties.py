from cipher_abc import CipherMethods, CipherOutput
from typing import Any
import string

class Rot17(CipherMethods):
    def __init__(self, obj: CipherOutput):
        self.obj = obj

    def encrypt_data(self, text_to_encrypt: str) -> Any: # DataClass ROT13/ROT47:
        text_to_encrypt = text_to_encrypt.lower()

        encrypted = []
        for char in text_to_encrypt:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + 17) % 26 + base)
                encrypted.append(new_char)
            else:
                encrypted.append(char)

        self.obj.text = text_to_encrypt
        self.obj.rot_type = "rot17"
        self.obj.status = 'encrypted'

        return ''.join(encrypted)


    def decrypt_data(self) -> Any:
        pass







