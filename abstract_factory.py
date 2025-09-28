from abc import ABC, abstractmethod
from dataclasses import dataclass

class CipherMethods(ABC):
    @abstractmethod
    def encrypt_data(self, input_str: str) -> str:
        pass

    @abstractmethod
    def decrypt_data(self) -> str:
        pass

@dataclass
class CipherABCData(ABC):
    text: str
    rot_type: str
    status: str






