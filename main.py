from logical_formula.truth_table import TruthTable


ts = r"(!(P→(P→(Q~Q))))"
# ts = r"(!(A∧B))"
# ts = r"((!((A→B12)∨((!C)∧D)))~(((!B)→C)~B))"
t = TruthTable(ts)
print(t.get_only_results())
print(t)
