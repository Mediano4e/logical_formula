import pandas as pd

from logical_formula.logical_formula import LogicalFormula


class TruthTable(object):
    def __init__(self, formula: str):
        self._formula = LogicalFormula(formula)
        self._result_table = self.__get_results_from_formula()
        self.__sort_table()
        del self._formula

    @property
    def results(self) -> pd.DataFrame:
        result = self._result_table
        if len(result.columns) == 1:
            return result
        return result.iloc[:, -1]

    @property
    def true_results(self) -> pd.DataFrame:
        table = self._result_table
        if len(table.columns) > 1:
            true_part = table.loc[table[table.columns[-1]]].iloc[:, :-1]
        else:
            true_part = table.loc[table[table.columns[-1]]]
        return true_part

    @property
    def false_results(self) -> pd.DataFrame:
        table = self._result_table
        if len(table.columns) > 1:
            false_part = table.loc[~table[table.columns[-1]]].iloc[:, :-1]
        else:
            false_part = table.loc[~table[table.columns[-1]]]
        return false_part

    @property
    def table(self) -> pd.DataFrame:
        return self._result_table

    def __get_results_from_formula(self) -> pd.DataFrame:
        table = pd.DataFrame(self._formula.table, index=[0])
        keys = self._formula.atomics_names
        length = len(keys)

        for i in range(2 ** length):
            for j in range(length):
                if i & (1 << j):
                    self._formula.switch(keys[j])
                    table.loc[len(table)] = self._formula.table
                    break
        return table

    @staticmethod
    def __count_sort_coefficients(line: pd.Series) -> int:
        length = len(line) - 1
        weight = 0
        for ind, val in enumerate(line):
            if val:
                weight += 2 ** (length - ind)
        return weight

    def __sort_table(self) -> None:
        table = self._result_table
        table['amount'] = table.apply(lambda row: row[:-1].sum(), axis=1)
        table['weight'] = table.apply(TruthTable.__count_sort_coefficients, axis=1)
        sorted_table = table.sort_values(by=['amount', 'weight'])
        sorted_table.drop(columns=['amount', 'weight'], inplace=True)
        sorted_table.reset_index(drop=True, inplace=True)
        self._result_table = sorted_table

    @staticmethod
    def __form_table_boarder(headers: dict, separators: tuple) -> str:
        boarder_string = separators[0]
        sizes = tuple(headers.values())
        for i in range(len(headers) - 1):
            boarder_string += "─" * sizes[i] + separators[1]

        boarder_string += "─" * sizes[-1] + separators[2] + "\n"

        return boarder_string

    @staticmethod
    def __form_headers(headers: dict) -> str:
        headers_string = ""
        for header in headers:
            headers_string += "│"
            free_space = headers[header] - len(header)
            interval = " " * (free_space // 2)
            if free_space % 2 == 1:
                headers_string += " "
            headers_string += interval + header + interval
        headers_string += "│\n"
        return headers_string

    @staticmethod
    def __form_index_part(headers: dict, index: int) -> str:
        index_part = ""
        free_space = headers["Index"] - len(str(index))
        if free_space % 2 == 1:
            index_part += " "
        interval = " " * (free_space // 2)
        index_part += interval + str(index) + interval + "│"
        return index_part

    def __form_line(self, headers: dict, line: pd.Series, index: int) -> str:
        line_string = "│"
        for header in headers:
            if header == "Index":
                line_string += TruthTable.__form_index_part(headers, index)
                continue
            interval = headers[header] // 2
            index = self._result_table.columns.get_loc(header)
            line_string += " " * interval + str(int(line[index]))

            if headers[header] % 2 == 0:
                interval -= 1
            line_string += " " * interval + "│"
        line_string += "\n"

        return line_string

    def __form_table(self, headers: dict) -> str:
        table_string = TruthTable.__form_table_boarder(headers, ("┌", "┬", "┐"))
        table_string += TruthTable.__form_headers(headers)

        for index, line in enumerate(self._result_table.values):
            table_string += TruthTable.__form_table_boarder(headers, ("├", "┼", "┤"))
            table_string += self.__form_line(headers, line, index)
        table_string += TruthTable.__form_table_boarder(headers, ("└", "┴", "┘"))

        return table_string

    def __form_str_table(self) -> str:
        headers = {name: len(name) + 2 for name in self._result_table.columns}
        largest_index = len(str(self._result_table.shape[0] - 1))
        index_column_size = len(str(largest_index)) if largest_index > 5 else 5
        headers = {"Index": index_column_size + 2} | headers
        length = sum(headers.values())
        length += len(headers) - 1
        return self.__form_table(headers)

    def __str__(self):
        return self.__form_str_table()
        # return str(self._result_table)
