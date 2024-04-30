from logical_formula.nodes import *


class LogicalFormula(object):
    def __init__(self, formula: str = "A"):
        self._atomics = dict()
        self._op_nodes = dict()
        self._operators = {"!": Negation, "∧": Conjunction, "∨": Disjunction, "→": Implication, "~": Equivalence}
        self._root = self.__convert(formula)
        self._result_table = self.__form_table(formula)
        del self._operators
        del self._op_nodes

    @property
    def atomics_names(self) -> list[str]:
        return list(self._atomics.keys())

    @property
    def result(self) -> bool:
        return self._root.value

    @property
    def table(self) -> dict:
        return self._result_table.copy()

    def switch(self, atomic_name: str) -> None:
        if atomic_name not in self._atomics:
            raise KeyError(f"Atomic node name '{atomic_name}' not found in atomic formulas.")

        self._atomics[atomic_name].update()
        self.__update_table(atomic_name)

    @staticmethod
    def __convert_const(formula: str) -> Node:
        if formula == "0":
            node = FalseNode()
        else:
            node = TrueNode()
        return node

    def __convert_atomic(self, formula: str) -> Node:
        if formula in self._atomics:
            node = self._atomics[formula]
        else:
            node = Atomic(formula)
            self._atomics[formula] = node
        return node

    def __convert_unary(self, formula: str) -> Node:
        if formula not in self._op_nodes:
            operand = self.__convert(formula[2:-1])
            node = Negation(operand)
            operand.add_parent(formula, node)
            self._op_nodes[formula] = node
        else:
            node = self._op_nodes[formula]
        return node

    def __parse_binary_logical_expression(self, formula: str, index: int) -> Node:
        operator = formula[index]
        if operator not in self._operators:
            raise ValueError(f"Unknown logical operator: {operator}")

        left_part, right_part = formula[1:index], formula[index+1:-1]
        left_operand, right_operand = self.__convert(left_part), self.__convert(right_part)

        node = self._operators[operator](left_operand, right_operand)

        left_operand.add_parent(formula, node)
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
            node = self.__convert_const(formula) if formula in ("0", "1") else self.__convert_atomic(formula)
        elif formula[1] in self._operators:
            node = self.__convert_unary(formula)
        else:
            node = self.__convert_binary(formula)

        return node

    def __form_table(self, formula: str) -> dict:
        table = dict()
        for atomic_name in self._atomics.keys():
            table[atomic_name] = False
        table[formula] = self.result
        return table

    def __update_table(self, atomic_name: str) -> None:
        self._result_table[atomic_name] = not self._result_table[atomic_name]
        self._result_table[str(self)] = self.result

    def __str__(self) -> str:
        return str(self._root)
