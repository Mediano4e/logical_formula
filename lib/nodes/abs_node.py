from abc import ABC, abstractmethod


class Node(ABC):
    @property
    @abstractmethod
    def value(self) -> bool:
        pass

    @abstractmethod
    def add_parent(self, parent_formula: str, parent) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
