from abstract_factory import CipherMethods, CipherABCData

class InputToEncrypt(CipherMethods):
    def __init__(self, data: CipherABCData) -> None:
        self.data = data

    def encrypt_data(self, input_str) -> str:
        self.data.text = input_str
        return self.data.text

    def decrypt_data(self) -> str:
        pass
