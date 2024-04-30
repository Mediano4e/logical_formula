import pandas as pd

from minimized_formulas.abs_minimizing_strategy import MinimizingStrategy
from minimized_formulas.shortening_method import ShorteningMethod


class CalculationMethod(MinimizingStrategy):
    @staticmethod
    def minimize(table: pd.DataFrame) -> pd.DataFrame:
        shorted = ShorteningMethod.shortening(table)
        return shorted[shorted.apply(CalculationMethod.__check_row, axis=1, table=shorted)]

    @staticmethod
    def __check_row(row: pd.Series, table: pd.DataFrame) -> bool:
        for index, value in row.items():
            if value is not None and not any(table.iloc[i][index] == value for i in range(len(table)) if i != row.name):
                return True
        return False
