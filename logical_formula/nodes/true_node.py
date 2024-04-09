from .abs_const import ConstNode


class TrueNode(ConstNode):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return "1"

    def get_value(self) -> bool:
        return True
