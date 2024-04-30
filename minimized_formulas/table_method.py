import pandas as pd

from logical_formula import TruthTable
from minimized_formulas.karnaugh_map import KMap
from minimized_formulas.calculation_table_method import CalcTableMethod
from minimized_formulas.abs_minimizing_strategy import MinimizingStrategy


class TableMethod(MinimizingStrategy):
    @staticmethod
    def minimize(table: pd.DataFrame):
        method = CalcTableMethod()
        result = method.minimize(table)
        return result
