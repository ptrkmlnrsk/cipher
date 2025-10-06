from dataclasses import dataclass

@dataclass
class Text:
    text: str
    rot_type: str
    status: str


class Buffer:
    def __init__(self):
        self.data: list[Text | str] = []

    def add(self, item: Text):
        self.data.append(item)

    def get_all(self) -> list[Text]:
        return self.data