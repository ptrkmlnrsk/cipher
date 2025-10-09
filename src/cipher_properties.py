from typing import Any

from src.cipher_abc import Cipher
from src.buffer import Text

class ROT13(Cipher):

    def cipher(self, text: str = None, shift: int=13) -> str:
        cipher_core_output = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + 13) % 26 + base)
                cipher_core_output.append(new_char)
            else:
                cipher_core_output.append(char)

        return ''.join(cipher_core_output)


    def encrypt_data(self, input_str: str) -> Text:

        # DataClass ROT13/ROT47:
        encryption_result = self.cipher(input_str)
        return Text(text=encryption_result,
                            rot_type = 'rot13',
                            status='encrypted')

    def decrypt_data(self, data: Text) -> Text: # cipher object or only text

        if data.status == 'encrypted':
            encryption_result = self.cipher(text=data.text,
                                        shift=-13)
            return Text(text=encryption_result,
                        rot_type='rot13',
                        status='decrypted')
        else:
            raise RuntimeError('Unknown rotation type.')


class ROT47(Cipher):

    def cipher(self, text: str = None, shift=47) -> str:
        cipher_core_output = []
        for char in text:
            code = ord(char)
            if 33 <= code <= 126:  # tylko znaki drukowalne ASCII
                new_char = chr(33 + ((code - 33 + 47) % 94))
                cipher_core_output.append(new_char)
            else:
                cipher_core_output.append(char)  # inne znaki zostają bez zmian

        return ''.join(cipher_core_output)

    def encrypt_data(self, input_str: str) -> Text:
        encryption_result = self.cipher(input_str)
        return Text(text=encryption_result,
                    rot_type='rot47',
                    status='encrypted')

    def decrypt_data(self, data: Any) -> Text:

        if data.status == 'encrypted':
            encryption_result = self.cipher(text=data.text,
                                        shift=-47)
            return Text(text=encryption_result,
                        rot_type='rot47',
                        status='decrypted')
        else:
            raise RuntimeError('Unknown rotation type.')



    #    return Text(text=data.text,
    #                        rot_type = data.rot_type,
    #                        status='decrypted')
    # def decrypt_data(self, data: Text) -> Text: # cipher object or only text
    #
    #     if data.status == 'encrypted':
    #         if data.rot_type == 'rot13':
    #             encryption_result = rot13_core(text=data.text,
    #                                         shift=-13)
    #             data.text = encryption_result
    #             #data.rot_type = 'rot13'
    #             data.status = 'decrypted'
    #
    #         elif data.rot_type == 'rot47':
    #             encryption_result = rot47_core(data.text,
    #                                            shift=-47)
    #             data.text = encryption_result
    #             data.rot_type = 'rot47'
    #             data.status = 'decrypted'
    #         else:
    #             raise RuntimeError('Unknown rotation type.')
    #
    #     return Text(text=data.text,
    #                         rot_type = data.rot_type,
    #                         status='decrypted')


