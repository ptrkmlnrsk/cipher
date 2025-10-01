from abc import ABC, abstractmethod
from dataclasses import dataclass

class CipherMethods(ABC):
    @abstractmethod
    def encrypt_data(self, input_str: str) -> str:
        # encrypting based on ROT
        pass

    @abstractmethod
    def decrypt_data(self) -> str:
        pass

@dataclass
class CipherOutput:
    text: str
    rot_type: str
    status: str


