from .abs_unary_op import UnaryOp
from .abs_node import Node


class Negation(UnaryOp):
    def __init__(self, operand: Node):
        super().__init__(operand)

    def __str__(self) -> str:
        return f"(!{str(self._operand)})"

    def solve(self) -> bool:
        return not self._operand.get_value()
