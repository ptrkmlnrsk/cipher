from typing import Any
from .rot_base import ROTBase
from .buffer import Text
from .const import ROT47_TYPE, ENCRYPTED, DECRYPTED


class ROT47(ROTBase):
    def cipher(self, text: str = None, shift=47) -> str:
        cipher_core_output = []
        for char in text:
            code = ord(char)
            if 33 <= code <= 126:  # tylko znaki drukowalne ASCII
                new_char = chr(33 + ((code - 33 + 47) % 94))
                cipher_core_output.append(new_char)
            else:
                cipher_core_output.append(char)  # inne znaki zostają bez zmian
        return "".join(cipher_core_output)

    def encrypt_data(self, input_str: str) -> Text:
        encryption_result = self.cipher(input_str)
        return Text(text=encryption_result, rot_type=ROT47_TYPE, status=ENCRYPTED)

    def decrypt_data(self, data: Any) -> Text:
        if data.status == ENCRYPTED:
            encryption_result = self.cipher(text=data.text, shift=-47)
            return Text(text=encryption_result, rot_type=ROT47_TYPE, status=DECRYPTED)
        else:
            raise RuntimeError("Unknown rotation type.")
