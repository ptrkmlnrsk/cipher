from typing import Any

from .rot_base import ROTBase
from .buffer import Text
from .const import ROT13_TYPE, ENCRYPTED, DECRYPTED


class ROT13(ROTBase):
    SHIFT = 13

    def cipher(self, shift: int, text: str = None) -> str:
        cipher_core_output = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                new_char = chr((ord(char) - base + shift) % 26 + base)
                cipher_core_output.append(new_char)
            else:
                cipher_core_output.append(char)
        return "".join(cipher_core_output)

    def encrypt_data(self, input_str: str) -> Text:
        encryption_result = self.cipher(shift=self.SHIFT, text=input_str)
        return Text(text=encryption_result, rot_type=ROT13_TYPE, status=ENCRYPTED)

    def decrypt_data(self, data: Any) -> Text:
        if data.status == ENCRYPTED:
            encryption_result = self.cipher(shift=-self.SHIFT, text=data.text)
            return Text(text=encryption_result, rot_type=ROT13_TYPE, status=DECRYPTED)
        else:
            raise RuntimeError("Unknown rotation type.")
