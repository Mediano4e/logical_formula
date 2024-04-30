from .abs_node import Node
from .abs_binary_op import BinaryOp


class Conjunction(BinaryOp):
    def __init__(self, left_op: Node, right_op: Node):
        super().__init__(left_op, right_op)

    def solve(self) -> bool:
        return self.left_op.value and self.right_op.value

    def __str__(self) -> str:
        return f"({str(self.left_op)}∧{str(self.right_op)})"
