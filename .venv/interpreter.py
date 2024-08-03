class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def interpret(self, node):
        if node[0] == 'program':
            for stmt in node[1]:
                self.interpret(stmt)
        elif node[0] == 'assign':
            self.variables[node[1]] = self.evaluate(node[2])
        elif node[0] == 'print':
            print(self.evaluate(node[1]))
        elif node[0] == 'if':
            condition = self.evaluate(node[1])
            if condition:
                self.interpret(('program', node[2]))
            else:
                for elseif in node[3]:
                    if elseif and self.evaluate(elseif[1]):
                        self.interpret(('program', elseif[2]))
                        return
                if node[4]:
                    self.interpret(('program', node[4]))
        elif node[0] == 'function':
            self.functions[node[1]] = (node[2], node[3])
        elif node[0] == 'return':
            raise ReturnException(self.evaluate(node[1]))
        elif node[0] == 'expression_statement':
            self.evaluate(node[1])
        elif node[0] == 'lambda':
            self.functions[node[1]] = (node[2], [('return',node[3])])
            self.variables[node[1]] = ('lambda',node[2], [('return',node[3])])



    def evaluate(self, node):
        if isinstance(node, int) or isinstance(node, bool):
            return node
        elif isinstance(node, str):
            if node in self.variables:
                return self.variables[node]
            elif node == 'True':
                return True
            elif node == 'False':
                return False
            else:
                raise NameError(f"Undefined variable '{node}'")
        elif node[0] == 'not':
            return not self.evaluate(node[1])
        elif node[0] == 'uminus':
            return -self.evaluate(node[1])
        elif node[0] == '+':
            return self.evaluate(node[1]) + self.evaluate(node[2])
        elif node[0] == '-':
            return self.evaluate(node[1]) - self.evaluate(node[2])
        elif node[0] == '*':
            return self.evaluate(node[1]) * self.evaluate(node[2])
        elif node[0] == '/':
            return (int) (self.evaluate(node[1]) / self.evaluate(node[2]))
        elif node[0] == '%':
            return self.evaluate(node[1]) % self.evaluate(node[2])
        elif node[0] == '>':
            return self.evaluate(node[1]) > self.evaluate(node[2])
        elif node[0] == '<':
            return self.evaluate(node[1]) < self.evaluate(node[2])
        elif node[0] == '>=':
            return self.evaluate(node[1]) >= self.evaluate(node[2])
        elif node[0] == '<=':
            return self.evaluate(node[1]) <= self.evaluate(node[2])
        elif node[0] == '==':
            return self.evaluate(node[1]) == self.evaluate(node[2])
        elif node[0] == '!=':
            return self.evaluate(node[1]) != self.evaluate(node[2])
        elif node[0] == '&&':
            return self.evaluate(node[1]) and self.evaluate(node[2])
        elif node[0] == '||':
            return self.evaluate(node[1]) or self.evaluate(node[2])
        elif node[0] == 'call':
            return self.call_function(node[1], node[2])
        elif node[0] == 'call_lambda':
            return self.call_lambda(node[1], node[2])
        elif node[0] == 'lambda':
            return ('lambda', node[1], node[2])

    def call_function(self, name, args):
        if name in self.functions:
            params, body = self.functions[name]
            if len(params) != len(args):
                raise Exception(f"Function '{name}' expects {len(params)} arguments but got {len(args)}")
            local_vars = self.variables.copy()
            for param, arg in zip(params, args):
                self.variables[param] = self.evaluate(arg)
            try:
                self.interpret(('program', body))
            except ReturnException as e:
                return e.value
            finally:
                self.variables = local_vars
        elif name in self.variables:
            lambda_info = self.variables[name]
            if lambda_info[0] == 'lambda':
                return self.call(lambda_info[1], lambda_info[2], args)
            else:
                raise Exception(f"'{name}' is not a function or lambda")
        else:
            raise Exception(f"Function '{name}' is not defined")

    def call_lambda(self, params, body, args):
        if len(params) != len(args):
            raise Exception(f"Lambda function expects {len(params)} arguments but got {len(args)}")
        local_vars = self.variables.copy()
        for param, arg in zip(params, args):
            self.variables[param] = self.evaluate(arg)
        try:
            return self.evaluate(body)
        finally:
            self.variables = local_vars

interpreter = Interpreter()
