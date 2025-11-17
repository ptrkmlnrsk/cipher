from src.helpers.text import Text
from typing import Any
from dataclasses import asdict


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

    def get_list_of_dicts(self) -> list[dict[str, Any]]:
        return [asdict(text_obj) for text_obj in self.data]

    def clear(self) -> None:
        self.data.clear()
