import pandas as pd

from abc import ABC, abstractmethod


class MinimizingStrategy(ABC):
    @staticmethod
    @abstractmethod
    def minimize(table: pd.DataFrame):
        pass
