from .abs_node import Node
from .abs_unary_op import UnaryOp


class Negation(UnaryOp):
    def __init__(self, operand: Node):
        super().__init__(operand)

    def solve(self) -> bool:
        return not self._operand.value

    def __str__(self) -> str:
        return f"(!{str(self._operand)})"
