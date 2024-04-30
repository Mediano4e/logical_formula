import pandas as pd


class KMap(object):
    def __init__(self, truth_table: pd.DataFrame):
        self._map = KMap._form_map(truth_table)

    @staticmethod
    def _form_map(truth_table: pd.DataFrame) -> pd.DataFrame:
        kmap = KMap._create_map(truth_table.columns)
        for ind, row in truth_table.iterrows():
            if not row.iloc[-1]:
                continue
            row_n, column_n = KMap._convert_to_cords(row)
            kmap.at[row_n, column_n] = "1"

        return kmap

    @staticmethod
    def _create_map(args: list[str]) -> pd.DataFrame:
        size = len(args) - 1 if len(args) > 1 else 1
        rows_num, columns_num = size // 2, size - size // 2
        rows_names, columns_names = KMap._generate_gray_codes(rows_num), KMap._generate_gray_codes(columns_num)
        kmap = pd.DataFrame("0", index=rows_names, columns=columns_names)
        return kmap

    @staticmethod
    def _generate_gray_codes(length: int) -> list[str]:
        if length <= 0:
            return []

        if length == 1:
            return ['0', '1']

        prev_gray_code = KMap._generate_gray_codes(length - 1)
        new_gray_code = []

        for code in prev_gray_code:
            new_gray_code.append('0' + code)
        for code in reversed(prev_gray_code):
            new_gray_code.append('1' + code)

        return new_gray_code

    @staticmethod
    def _convert_to_cords(row) -> (str, str):
        row_cord, column_cord = "", ""
        for i in range(len(row) - 1):
            if i < (len(row) - 1) // 2:
                row_cord += "1" if row.iloc[i] else "0"
                continue
            column_cord += "1" if row.iloc[i] else "0"
        return row_cord, column_cord

    def __str__(self) -> str:
        return str(self._map)
