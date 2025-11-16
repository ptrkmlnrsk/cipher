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

    def clear(self) -> None:
        self.data.clear()

    @staticmethod
    def data_append_helper(data_to_append_to: dict, data_to_append: Any) -> dict:
        data_to_append_to["result"].extend(
            [asdict(text_obj) for text_obj in data_to_append]
        )
        return data_to_append_to
