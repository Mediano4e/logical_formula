from abc import abstractmethod

from .abs_node import Node


class VariableNode(Node):
    def __init__(self, value: bool = False):
        super().__init__()
        self._value = value
        self._parents = dict()

    @abstractmethod
    def update(self) -> None:
        pass

    @property
    def value(self) -> bool:
        return self._value

    def add_parent(self, parent_formula: str, parent) -> None:
        if parent_formula not in self._parents:
            self._parents[parent_formula] = parent

    def _invert_value(self) -> None:
        self._value = not self._value

    def _call_updates(self) -> None:
        for parent in self._parents.values():
            parent.update()
