from .abs_const import ConstNode


class TrueNode(ConstNode):
    def __init__(self):
        super().__init__()

    @property
    def value(self) -> bool:
        return True

    def __str__(self) -> str:
        return "1"
