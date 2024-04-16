from lib.truth_table import TruthTable


# ts = r"(!(P→(P→(Q~Q))))"
# ts = r"(!(A∧B))"
ts = r"((!((A→B12)∨((!C)∧D)))~(((!B)→C)~B))"
t = TruthTable(ts)
print(t.results)
print(t)
print(t.true_results)
print(t.false_results)
