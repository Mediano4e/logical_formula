from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_value(self) -> bool:
        pass
