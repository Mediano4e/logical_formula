from .abs_const import ConstNode


class FalseNode(ConstNode):
    def __init__(self):
        super().__init__()

    @property
    def value(self) -> bool:
        return False

    def __str__(self) -> str:
        return "0"
