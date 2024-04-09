import pandas as pd
from .logical_formula import LogicalFormula


class TruthTable(object):
    def __init__(self, formula: str):
        self._formula = LogicalFormula(formula)
        self._result = self.__get_results_from_formula()
        self._table_string = ""
        del formula

    def __get_results_from_formula(self) -> pd.DataFrame:
        columns = self._formula.get_full_result().index
        table = pd.DataFrame(columns=columns)
        keys = list(self._formula.get_atomics().keys())
        table.loc[len(table)] = self._formula.get_full_result()
        length = len(keys)

        for i in range(2 ** length):
            for j in range(length):
                if i & (1 << j):
                    self._formula.switch(keys[j])
                    table.loc[len(table)] = self._formula.get_full_result()
                    break
        return table

    def get_short_result(self) -> pd.DataFrame:
        atomics_amount = len(self._formula.get_atomics())
        formulas = list(self._result.columns)
        keys = formulas[:atomics_amount] + [formulas[-1]]

        return self._result[keys]

    def get_only_results(self) -> list:
        return list(self._result.iloc[:, -1])

    @staticmethod
    def __form_table_boarder(headers: dict, separators: tuple):
        boarder_string = separators[0]
        sizes = tuple(headers.values())
        for i in range(len(headers) - 1):
            boarder_string += "─" * sizes[i] + separators[1]

        boarder_string += "─" * sizes[-1] + separators[2] + "\n"

        return boarder_string

    def __form_line(self, headers: dict, line: pd.Series):
        line_string = "│"
        for header in headers:
            index = self._result.columns.get_loc(header)
            interval = headers[header] // 2
            line_string += " " * interval + str(int(line[index]))

            if headers[header] % 2 == 0:
                interval -= 1
            line_string += " " * interval + "│"
        line_string += "\n"

        return line_string

    def __form_table(self, headers: dict):
        table_string = TruthTable.__form_table_boarder(headers, ("┌", "┬", "┐"))
        table_string += "│" + "│".join([" " + header + " " for header in headers]) + "│" + "\n"

        for line in self._result.values:
            table_string += TruthTable.__form_table_boarder(headers, ("├", "┼", "┤"))
            table_string += self.__form_line(headers, line)
        table_string += TruthTable.__form_table_boarder(headers, ("└", "┴", "┘"))

        return table_string

    def form_result_table(self):
        table = self.get_short_result()
        headers_keys = table.columns
        headers = {name: len(name) + 2 for name in headers_keys}
        return self.__form_table(headers)

    def form_full_table(self):
        headers = {name: len(name)+2 for name in self._result.columns}
        length = sum(headers.values())
        length += len(headers) - 1
        return self.__form_table(headers)

    def __str__(self):
        return self.form_full_table()
