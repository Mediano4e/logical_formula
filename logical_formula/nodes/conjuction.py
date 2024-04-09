from .abs_binary_op import BinaryOp
from .abs_node import Node


class Conjunction(BinaryOp):
    def __init__(self, left_op: Node, right_op: Node):
        super().__init__(left_op, right_op)

    def __str__(self) -> str:
        return f"({str(self.left_op)}∧{str(self.right_op)})"

    def solve(self) -> bool:
        return self.left_op.get_value() and self.right_op.get_value()
