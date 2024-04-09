from .abs_operator import OperatorNode
from .abs_node import Node


class BinaryOp(OperatorNode):
    def __init__(self, left_operand: Node, right_operand: Node):
        self.left_op = left_operand
        self.right_op = right_operand
        value = self.solve()
        super().__init__(value)
