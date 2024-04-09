from .abs_operator import OperatorNode
from .abs_node import Node


class UnaryOp(OperatorNode):
    def __init__(self, operand: Node):
        self._operand = operand
        value = self.solve()
        super().__init__(value)
