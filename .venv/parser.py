# parser.py
import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_statement
                 | print_statement
                 | if_statement
                 | assignment_statement
                 | function_definition
                 | return_statement'''
    p[0] = p[1]

def p_function_definition(p):
    '''function_definition : ZAP ID LPAREN param_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function_definition', p[2], p[4], p[7])

def p_param_list(p):
    '''param_list : ID
                  | param_list COMMA ID
                  | empty'''
    if len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_return_statement(p):
    '''return_statement : RETURN expression SEMI'''
    p[0] = ('return', p[2])

def p_print_statement(p):
    '''print_statement : PRINT expression SEMI'''
    p[0] = ('print', p[2])

def p_if_statement(p):
    '''if_statement : IF expression LBRACE statement_list RBRACE
                    | IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 6:
        p[0] = ('if', p[2], p[4])
    else:
        p[0] = ('if_else', p[2], p[4], p[8])

def p_assignment_statement(p):
    '''assignment_statement : ID ASSIGN expression SEMI'''
    p[0] = ('assign', p[1], p[3])

def p_expression_statement(p):
    '''expression_statement : expression SEMI'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

def p_expression_uminus(p):
    '''expression : MINUS expression %prec UMINUS'''
    p[0] = ('uminus', p[2])

def p_expression_function_call(p):
    '''expression : ID LPAREN arg_list RPAREN'''
    p[0] = ('call', p[1], p[3])

def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression
                | empty'''
    if len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

