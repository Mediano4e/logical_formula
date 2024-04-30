import pandas as pd


class ShorteningMethod(object):
    @staticmethod
    def shortening(table: pd.DataFrame) -> pd.DataFrame:
        res_table = pd.DataFrame(columns=table.columns)

        for i in range(len(table) - 1):
            for j in range(i + 1, len(table)):
                diff_count = (table.iloc[i].ne(table.iloc[j])).sum()
                if diff_count == 1:
                    new_row = table.iloc[i].where(table.iloc[i] == table.iloc[j], None)
                    res_table.loc[len(res_table)] = new_row

        return res_table
