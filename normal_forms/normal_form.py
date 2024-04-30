import pandas as pd

from logical_formula import TruthTable


class NormalFormula(object):
    def __init__(self, formula: str):
        self.table = TruthTable(formula)

    @property
    def numeric_form(self):
        table = self.table.true_results
        indexes = table.index
        val_list = [int(x) for x in indexes]
        print(val_list)
        return sum(val_list)

    @property
    def index_form(self):
        length = len(self.table.table.index)
        true_table = self.table.true_results
        indexes = true_table.index
        val_list = [2**(length - int(x) - 1) for x in indexes]
        print(val_list)
        return sum(val_list)

    @property
    def pdnf(self) -> str:
        res = ""
        table = self.table.true_results
        if table.empty:
            return res
        for i, row in table.iterrows():
            res += NormalFormula.__create_part(row, "∧") + "∨"

        return res[:-1]

    @property
    def pcnf(self) -> str:
        res = ""
        table = self.table.false_results
        if table.empty:
            return res
        for i, row in table.iterrows():
            res += NormalFormula.__create_part(row, "∨") + "∧"

        return res[:-1]

    @staticmethod
    def __create_part(table_part: pd.Series, connector: str) -> str:
        part = ""
        if table_part.empty:
            return part
        for i, val in table_part.items():
            if val:
                part += str(i)
            else:
                part += "(!" + str(i) + ")"
            part += connector
        return "(" + part[0:-1] + ")"

    def __str__(self) -> str:
        return "PDNF: " + self.pdnf + "\n" + "PCNF: " + self.pcnf + \
            "\n" + "Index form: " + str(self.index_form) + "\n" + \
            "Numeric form: " + str(self.numeric_form)
