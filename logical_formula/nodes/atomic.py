import pandas as pd
from .abs_variable import VariableNode


class Atomic(VariableNode):
    def __init__(self, name: str, value: bool = False):
        super().__init__(value)
        self._name = name

    def __str__(self) -> str:
        return self._name

    def get_value(self) -> bool:
        return self._value

    def update(self) -> pd.Series:
        self._invert_value()
        return self._get_changes()
