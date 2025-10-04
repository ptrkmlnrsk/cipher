from cipher_abc import CipherMethods, CipherOutput
from typing import Any, Callable
from cipher_core import rot13_core, rot47_core
import string

class CaesarRots(CipherMethods):
    def __init__(self, obj: CipherOutput):
        self.obj = obj

    def encrypt_data(self, input_str: str, rot: str='rot13') -> str|list: # DataClass ROT13/ROT47:

        if self.obj.status != 'ENCRYPTED':
            if rot == 'rot13':
                encryption_result = rot13_core(input_str)
                self.obj.text = encryption_result
                self.obj.rot_type = rot
                self.obj.status = 'ENCRYPTED'

            elif rot == 'rot47':
                encryption_result = rot47_core(input_str)
                self.obj.text = encryption_result
                self.obj.rot_type = rot
                self.obj.status = 'ENCRYPTED'

            else:
                raise NameError('You need to provide exactly rot13 or rot47')

        return self.obj.text


    def decrypt_data(self) -> Any: # cipher object or only text

        if self.obj.status == 'ENCRYPTED':
            if self.obj.rot_type == 'rot13':
                encryption_result = rot13_core(text=self.obj.text,
                                            shift=-13)
                self.obj.text = encryption_result
                self.obj.rot_type = 'rot13'
                self.obj.status = 'DECRYPTED'

            elif self.obj.rot_type == 'rot_47':
                encryption_result = rot47_core(self.obj.text,
                                               shift=-47)
                self.obj.text = encryption_result
                self.obj.rot_type = 'rot47'
                self.obj.status = 'DECRYPTED'
            else:
                raise RuntimeError('Unknown rotation type.')

        return self.obj.text

# classmethod???? boilerplating??
#class Rot47(CipherMethods):
#    def __init__(self, obj: CipherOutput):
#        self.obj = obj#
#
#    def encrypt_data(self, input_str: str) -> str:
#        if self.obj.status != 'ENCRYPTED':
#            encryption_result = rot47_core(input_str)

#            self.obj.text = encryption_result
#           self.obj.rot_type = 'rot47'
#           self.obj.status = 'ENCRYPTED'

#        return self.obj.text
#
#   def decrypt_data(self) -> str:
#       if self.obj.status == 'ENCRYPTED':
#            encryption_result = rot47_core(self.obj.text,
#                                           shift=-47)

#            self.obj.text = encryption_result
#            self.obj.rot_type = 'rot47'
#            self.obj.status = 'DECRYPTED'

#        return self.obj.text







