from .abs_node import Node
from abc import abstractmethod
import pandas as pd


class VariableNode(Node):
    def __init__(self, value: bool = False):
        super().__init__()
        self._value = value
        self._parents = dict()

    def get_value(self) -> bool:
        return self._value

    def _invert_value(self) -> None:
        self._value = not self._value

    def _get_changes(self) -> dict:
        changed_values = dict()
        changed_values[str(self)] = self._value
        for parent in self._parents.values():
            changed_values = changed_values | parent.update()
        return changed_values

    def add_parent(self, parent_formula: str, parent) -> None:
        if parent_formula not in self._parents:
            self._parents[parent_formula] = parent

    @abstractmethod
    def update(self) -> pd.Series:
        pass
