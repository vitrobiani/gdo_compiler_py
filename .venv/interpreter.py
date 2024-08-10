class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class FunctionParameters(Exception):
    pass

class BlankException(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def interpret(self, node):
        if node[0] == 'program':
            for stmt in node[1]:
                self.interpret(stmt)
        elif node[0] == 'assign':
            try:
                self.variables[node[1]] = self.evaluate(node[2])
            except Exception as e:
                raise Exception(f'{e}, at line number {node[-1]}')
        elif node[0] == 'println':
            try:
                print(self.evaluate(node[1]))
            except BlankException:
                print()
            except Exception as e:
                raise Exception(f'{e}, at line number {node[-1]}')
        elif node[0] == 'print':
            try:
                print(self.evaluate(node[1]), end=" ")
            except Exception as e:
                raise Exception(f'{e}, at line number {node[-1]}')
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
            try:
                self.functions[node[1]] = (node[2], node[3])
            except Exception as e:
                raise Exception(f'{e}, at line number {node[-1]}')
        elif node[0] == 'return':
            if node[1] == None:
                return
            raise ReturnException(self.evaluate(node[1]))
        elif node[0] == 'expression_statement':
            try:
                self.evaluate(node[1])
            except Exception as e:
                raise Exception(f'{e}, at line number {node[-1]}')
        elif node[0] == 'lambda':
            # self.functions[node[1]] = (node[2], [('return',node[3])])
            self.variables[node[1]] = ('lambda',node[2])
        elif node[0] == 'call':
            self.evaluate(node)


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
        elif node == None:
            raise BlankException("Blank space where it shoudn't be")
        if node[0] == 'not':
            return not self.evaluate(node[1])
        elif node[0] == 'uminus':
            return -self.evaluate(node[1])
        elif node[0] == '+':
            if isinstance(self.evaluate(node[1]), bool):
                raise TypeError(f"'{node[1]}' Wrong Type")
            if  isinstance(self.evaluate(node[2]), bool):
                raise TypeError(f"'{node[2]}' Wrong Type")
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
            try:
                return self.call_function(node[1], node[2])
            except FunctionParameters as e:
                raise Exception(f'{e}, at line number {node[-1]}')

    def call_function(self, name, args):
        if name in self.functions:
            params, body = self.functions[name]
            if len(params) != len(args):
                raise FunctionParameters(f"Function '{name}' expects {len(params)} arguments but got {len(args)}")
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
                return self.call_lambda(lambda_info[1][1], lambda_info[1][2], args)
            else:
                raise Exception(f"'{name}' is not a function or lambda")
        else:
            raise Exception(f"Function '{name}' is not defined")

    def call_lambda(self, params, body, args):
        if len(params) != len(args):
            raise Exception(f"Lambda function expects '{len(params)}' arguments but got '{len(args)}'")
        local_vars = self.variables.copy()
        for param, arg in zip(params, args):
            self.variables[param] = self.evaluate(arg)
        try:
            return self.evaluate(body)
        finally:
            self.variables = local_vars

interpreter = Interpreter()
