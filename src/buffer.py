from dataclasses import dataclass
from typing import Any


@dataclass
class Text:
    text: str
    rot_type: str
    status: str


class Buffer:
    def __init__(self):
        self.data: list[Text | dict[str, Any]] = []

    def add(self, item: Text | dict[str, Any]) -> None:
        self.data.append(item)

    def get_all(self) -> list[Text]:
        return self.data
