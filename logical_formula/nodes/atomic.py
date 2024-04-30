from .abs_variable import VariableNode


class Atomic(VariableNode):
    def __init__(self, name: str, value: bool = False):
        super().__init__(value)
        self._name = name

    def get_value(self) -> bool:
        return self._value

    def update(self) -> None:
        self._invert_value()
        self._call_updates()

    def __str__(self) -> str:
        return self._name
