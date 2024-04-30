import pandas as pd

from logical_formula import TruthTable
from minimized_formulas.calculation_method import CalculationMethod
from minimized_formulas.calculation_table_method import CalcTableMethod
from minimized_formulas.table_method import TableMethod


class Minimized(object):
    def __init__(self, formula: str):
        self._tt = TruthTable(formula)
        self._methods = [CalcTableMethod(), CalculationMethod(), TableMethod()]
        self._method_num = 0

    @property
    def mdnf(self):
        table = self._tt.true_results
        minimized = self._methods[0].minimize(table)


    @property
    def mcnf(self):
        table = self._tt.false_results
        minimized = self._methods[0].minimize(table)

    def _form_part(self):
        pass

    def __str__(self):
        pass
