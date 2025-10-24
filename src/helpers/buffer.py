from src.helpers.text_dataclass import Text
from typing import Any


class Buffer:
    def __init__(self):
        self.data: list[Text | dict[str, Any]] = []

    def add(self, item: Text | dict[str, Any] | list) -> None:
        if isinstance(item, (dict, Text)):
            self.data.append(item)
        else:
            self.data.extend(item)

    def get_all(self) -> list[Text]:
        return self.data

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def clear(self) -> None:
        self.data.clear()
