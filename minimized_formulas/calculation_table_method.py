import pandas as pd

from minimized_formulas.abs_minimizing_strategy import MinimizingStrategy
from minimized_formulas.shortening_method import ShorteningMethod


class CalcTableMethod(MinimizingStrategy):
    @staticmethod
    def minimize(table: pd.DataFrame) -> pd.DataFrame:
        # print(table)
        shorted = ShorteningMethod.shortening(table)
        # print(shorted)
        mapping = CalcTableMethod.__table_mapping(shorted, table)
        # print(mapping)
        res = mapping[mapping.apply(CalcTableMethod.__check_row, axis=1, table=mapping)]
        # print(res)
        return shorted.loc[res.index]

    @staticmethod
    def __table_mapping(table1: pd.DataFrame, table2: pd.DataFrame) -> pd.DataFrame:
        mapping = pd.DataFrame(False, index=range(len(table1)), columns=range(len(table2)))

        for i, row1 in table1.iterrows():
            for j, row2 in table2.iterrows():
                if all(x == y or pd.isna(x) for x, y in zip(row1, row2)):
                    mapping.loc[i, j] = True

        return mapping

    @staticmethod
    def __check_row(row: pd.Series, table: pd.DataFrame) -> bool:
        for index, value in row.items():
            if value is not None and not any(table.iloc[i][index] == value for i in range(len(table)) if i != row.name):
                return True
        return False
