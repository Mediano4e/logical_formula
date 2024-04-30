import pandas as pd
from minimized_formulas.calculation_method import CalculationMethod
from minimized_formulas.calculation_table_method import CalcTableMethod
from minimized_formulas.table_method import TableMethod


# Пример данных
data = pd.DataFrame({
    'A': [False, False, False, True],
    'B': [False, True, True, True],
    'C': [True, False, True, False]
})


# data = pd.DataFrame({
#     'A': [False, True, True, True],
#     'B': [False, False, False, True],
#     'C': [False, False, True, True]
# })


table = CalculationMethod.minimize(data)
print(table)
print("="*183)

table2 = CalcTableMethod.minimize(data)
print(table2)

print("="*183)
data2 = pd.DataFrame({
    'A': [False, False, False, True],
    'B': [False, True, True, True],
    'C': [True, False, True, False],
    "Result": [True, False, True, True]
})

table3 = TableMethod.minimize(data)
print(table3)

# def generate_gray_code(length):
#     if length <= 0:
#         return []
#
#     if length == 1:
#         return ['0', '1']
#
#     prev_gray_code = generate_gray_code(length - 1)
#     new_gray_code = []
#
#     for code in prev_gray_code:
#         new_gray_code.append('0' + code)
#     for code in reversed(prev_gray_code):
#         new_gray_code.append('1' + code)
#
#     return new_gray_code
#
# # Пример использования:
# length = 5
# gray_codes = generate_gray_code(length)
# print("Gray Codes of length", length, "are:", gray_codes)

# from logical_formula import TruthTable
# from minimized_formulas.karnaugh_map import KMap
#
#
# # ts = "((!((A→B)∨((!C)∧D)))~(((!B)→C)~B))"
# ts = "((((A~B)~C)~D)~E)"
# # ts = "((A~B)~C)"
# tt = TruthTable(ts)
# t = KMap(tt.table)
# print(t)
