from cipher_abc import CipherMethods, CipherOutput
from cipher_core import rot13_core, rot47_core

class CaesarRots(CipherMethods):

    def encrypt_data(self, *, input_str: str) -> CipherOutput:

        # DataClass ROT13/ROT47:
        encryption_result = rot13_core(input_str)
        return CipherOutput(text=encryption_result,
                            rot_type = 'rot13',
                            status='encrypted')

    def decrypt_data(self, data: CipherOutput) -> CipherOutput: # cipher object or only text

        if data.status == 'encrypted':
            if data.rot_type == 'rot13':
                encryption_result = rot13_core(text=data.text,
                                            shift=-13)
                data.text = encryption_result
                #data.rot_type = 'rot13'
                data.status = 'decrypted'

            elif data.rot_type == 'rot47':
                encryption_result = rot47_core(data.text,
                                               shift=-47)
                data.text = encryption_result
                data.rot_type = 'rot47'
                data.status = 'decrypted'
            else:
                raise RuntimeError('Unknown rotation type.')

        return CipherOutput(text=data.text,
                            rot_type = data.rot_type,
                            status='decrypted')
