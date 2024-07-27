class Interpreter:
    def __init__(self):
        self.global_env = {}
        self.call_stack = []

    def interpret(self, node):
        node_type = node[0]
        if node_type == 'program':
            for statement in node[1]:
                self.interpret(statement)
        elif node_type == 'assign':
            var_name = node[1]
            var_value = self.evaluate(node[2])
            self.global_env[var_name] = var_value
        elif node_type == 'binop':
            left_value = self.evaluate(node[2])
            right_value = self.evaluate(node[3])
            return self._apply_binop(node[1], left_value, right_value)
        elif node_type == 'uminus':
            return -self.evaluate(node[1])
        elif node_type == 'number':
            return node[1]
        elif node_type == 'id':
            return self.global_env.get(node[1], 0)
        elif node_type == 'if':
            condition = self.evaluate(node[1])
            if condition:
                self.interpret(node[2])
        elif node_type == 'if_else':
            condition = self.evaluate(node[1])
            if condition:
                self.interpret(node[2])
            else:
                self.interpret(node[3])
        elif node_type == 'print':
            value = self.evaluate(node[1])
            print(value)
        elif node_type == 'return':
            raise ReturnException(self.evaluate(node[1]))
        elif node_type == 'function_definition':
            func_name = node[1]
            params = node[2]
            body = node[3]
            self.global_env[func_name] = ('lambda', params, body)
        elif node_type == 'call':
            func = self.global_env.get(node[1])
            if func is None or func[0] != 'lambda':
                raise Exception(f"'{node[1]}' is not a callable function")
            args = [self.evaluate(arg) for arg in node[2]]
            return self._call_function(func, args)

    def evaluate(self, node):
        return self.interpret(node)

    def _apply_binop(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '>':
            return int(left > right)
        elif operator == '<':
            return int(left < right)
        elif operator == '>=':
            return int(left >= right)
        elif operator == '<=':
            return int(left <= right)
        elif operator == '==':
            return int(left == right)

    def _call_function(self, func, args):
        param_names, body = func[1], func[2]
        local_env = self.global_env.copy()
        for param_name, arg in zip(param_names, args):
            local_env[param_name] = arg
        self.call_stack.append(self.global_env)
        self.global_env = local_env
        try:
            self.interpret(body)
        except ReturnException as e:
            return e.value
        finally:
            self.global_env = self.call_stack.pop()


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
