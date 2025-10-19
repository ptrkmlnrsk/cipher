from abc import ABC, abstractmethod
from typing import Any


class ROTBase(ABC):  # Cipher
    @abstractmethod
    def cipher(self, shift: int, text: str):
        pass

    @abstractmethod
    def encrypt_data(self, input_str: str) -> str:
        # encrypting based on ROT
        pass

    @abstractmethod
    def decrypt_data(self, data: Any) -> str:
        pass
