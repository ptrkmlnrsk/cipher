from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

class Cipher(ABC): # Cipher

    @abstractmethod
    def cipher(self):
       pass

    @abstractmethod
    def encrypt_data(self, input_str: str) -> str:
        # encrypting based on ROT
        pass

    @abstractmethod
    def decrypt_data(self, data: Any) -> str:
        pass
