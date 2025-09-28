from abstract_factory import CipherABCData

class CipherData(CipherABCData):
    def __init__(self, text: str, rot_type: str, status: str):
        self.text = text
        self.rot_type = rot_type
        self.status = status



