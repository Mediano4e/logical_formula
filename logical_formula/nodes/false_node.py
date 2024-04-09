from .abs_const import ConstNode


class FalseNode(ConstNode):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "0"

    def get_value(self) -> bool:
        return False
