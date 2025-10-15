from typing import Any
from .rot_base import ROTBase
from .buffer import Text
from .const import ROT13_TYPE, ENCRYPTED, DECRYPTED


class ROT13(ROTBase):
    def cipher(self, text: str = None, shift: int = 13) -> str:
        cipher_core_output = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                new_char = chr((ord(char) - base + 13) % 26 + base)
                cipher_core_output.append(new_char)
            else:
                cipher_core_output.append(char)
        return "".join(cipher_core_output)

    def encrypt_data(self, input_str: str) -> Text:
        encryption_result = self.cipher(input_str)
        return Text(text=encryption_result, rot_type=ROT13_TYPE, status=ENCRYPTED)

    def decrypt_data(self, data: Any) -> Text:  # TODO brak spojnosci z rot47
        if data.status == ENCRYPTED:
            encryption_result = self.cipher(text=data.text, shift=-13)
            return Text(text=encryption_result, rot_type=ROT13_TYPE, status=DECRYPTED)
        else:
            raise RuntimeError("Unknown rotation type.")
