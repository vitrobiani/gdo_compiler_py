class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        node_type = node[0]
        if node_type == 'program':
            for statement in node[1]:
                self.analyze(statement)
        elif node_type == 'assign':
            var_name = node[1]
            var_value = self.analyze(node[2])
            self.symbol_table[var_name] = var_value
        elif node_type == 'binop':
            left_type = self.analyze(node[2])
            right_type = self.analyze(node[3])
            return self._check_binop(node[1], left_type, right_type)
        elif node_type == 'uminus':
            expr_type = self.analyze(node[1])
            if expr_type != 'int':
                raise Exception("Unary minus can only be applied to integers")
            return 'int'
        elif node_type == 'number':
            return 'int'
        elif node_type == 'id':
            var_type = self.symbol_table.get(node[1], 'undefined')
            if var_type == 'undefined':
                raise Exception(f"Variable '{node[1]}' is not defined")
            return var_type
        elif node_type == 'call':
            func_type = self.analyze(('id', node[1]))
            if func_type != 'lambda':
                raise Exception(f"'{node[1]}' is not callable")
            return 'int'
        elif node_type == 'if' or node_type == 'if_else':
            condition_type = self.analyze(node[1])
            if condition_type != 'int':
                raise Exception("Condition in 'if' statement must be an integer")
            self.analyze(node[2])
            if node_type == 'if_else':
                self.analyze(node[3])
        elif node_type == 'print':
            expr_type = self.analyze(node[1])
            if expr_type == 'undefined':
                raise Exception("Cannot print undefined variable")
        elif node_type == 'function_definition':
            func_name = node[1]
            params = node[2]
            body = node[3]
            self.symbol_table[func_name] = ('lambda', params, body)

    def _check_binop(self, operator, left_type, right_type):
        if left_type != 'int' or right_type != 'int':
            raise Exception(f"Operator {operator} requires integer operands")
        return 'int'
