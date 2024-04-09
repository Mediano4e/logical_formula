import pandas as pd
from .abs_variable import VariableNode
from abc import abstractmethod


class OperatorNode(VariableNode):
    def __init__(self, value: bool = False):
        super().__init__(value)

    def update(self) -> dict:
        if self._value == self.solve():
            return dict()
        self._invert_value()
        return self._get_changes()

    @abstractmethod
    def solve(self):
        pass
