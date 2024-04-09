import pandas as pd
from .nodes import *
from .nodes.abs_const import ConstNode


class LogicalFormula(object):
    def __init__(self, formula: str = "F"):
        self._atomics = dict()
        self._op_nodes = dict()
        self._full_result = pd.Series()
        self._operators = {"!": Negation, "∧": Conjunction, "∨": Disjunction, "→": Implication, "~": Equivalence}
        self._root = self.__convert(formula)
        sorted_pairs = sorted(self._full_result.items(), key=lambda x: self.__count_chars_in_key(x[0]))
        self._full_result = pd.Series([pair[1] for pair in sorted_pairs], index=[pair[0] for pair in sorted_pairs])
        del self._operators
        del self._op_nodes

    def __str__(self) -> str:
        return str(self._root)

    def get_atomics(self):
        return self._atomics.copy()

    def get_result(self) -> bool:
        return self._root.get_value()

    def get_full_result(self) -> pd.Series:
        return self._full_result.copy()

    def __count_chars_in_key(self, key):
        ops_count = sum(1 for char in key if char in self._operators)
        unary_count = sum(-1 for char in key if char == "!" or char == "¬")
        total_size = len(key)
        return ops_count, unary_count, total_size

    @staticmethod
    def __convert_const(formula: str) -> Node:
        if formula == "0":
            node = FalseNode()
        else:
            node = "1"
        return node

    def __convert_atomic(self, formula: str) -> Node:
        if formula in self._atomics:
            node = self._atomics[formula]
        else:
            node = Atomic(formula)
            self._atomics[formula] = node
        return node

    def __convert_unary(self, formula: str) -> Node:
        operand = self.__convert(formula[2:-1])
        node = Negation(operand)
        if not isinstance(operand, ConstNode):
            operand.add_parent(formula, node)
        self._op_nodes[formula] = node
        return node

    def __parse_binary_logical_expression(self, formula: str, index: int) -> Node:
        char = formula[index]
        if char not in self._operators:
            raise ValueError(f"Unknown logical operator: {char}")

        left_part, right_part = formula[1:index], formula[index+1:-1]
        left_operand, right_operand = self.__convert(left_part), self.__convert(right_part)

        node = self._operators[char](left_operand, right_operand)

        if not isinstance(left_operand, ConstNode):
            left_operand.add_parent(formula, node)
        if not isinstance(right_operand, ConstNode):
            right_operand.add_parent(formula, node)

        return node

    def __convert_binary(self, formula: str) -> Node:
        node: Node = FalseNode()
        level = 0
        for index, char in enumerate(formula):
            if (level == 1) and (char in self._operators):
                node = self.__parse_binary_logical_expression(formula, index)
                self._op_nodes[formula] = node
                break

            if char == "(":
                level += 1
            if char == ")":
                level -= 1
        return node

    def __convert(self, formula: str) -> Node:
        if formula in self._op_nodes:
            return self._op_nodes[formula]

        if formula[0] != "(":
            if formula in ("0", "1"):
                node = self.__convert_const(formula)
            else:
                node = self.__convert_atomic(formula)
        elif formula[1] in self._operators:
            node = self.__convert_unary(formula)
        else:
            node = self.__convert_binary(formula)

        if formula not in ("0", "1"):
            self._full_result[formula] = node.get_value()

        return node

    def __update_full_result(self, new_results: pd.Series) -> None:
        for key in new_results:
            if key in self._full_result:
                self._full_result[key] = new_results[key]

    def switch(self, atomic_name: str) -> None:
        if atomic_name not in self._atomics:
            raise KeyError(f"Atomic node name '{atomic_name}' not found in atomic formulas.")

        changes = self._atomics[atomic_name].update()
        self.__update_full_result(changes)
