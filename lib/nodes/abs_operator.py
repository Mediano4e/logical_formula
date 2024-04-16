from abc import abstractmethod

from .abs_variable import VariableNode


class OperatorNode(VariableNode):
    def __init__(self, value: bool = False):
        super().__init__(value)

    @abstractmethod
    def solve(self):
        pass

    def update(self) -> None:
        if self._value == self.solve():
            return
        self._invert_value()
        self._call_updates()
