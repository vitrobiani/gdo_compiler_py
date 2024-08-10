from lexer import tokens
import ply.yacc as yacc

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'GT', 'LT', 'GE', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
    ('right', 'ASSIGN')
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
    '''statement : assignment_statement
                 | print_statement
                 | if_statement
                 | function_definition
                 | return_statement
                 | expression_statement
                 | lambda_expression
                 | comment'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3], p.lineno(1))

def p_print_statement(p):
    '''print_statement : PRINTLN LPAREN expression RPAREN SEMICOLON
                       | PRINTLN LPAREN empty RPAREN SEMICOLON
                       | PRINT LPAREN expression RPAREN SEMICOLON
                       | PRINT LPAREN empty SEMICOLON'''
    if p[1] == 'print':
        p[0] = ('print', p[3], p.lineno(1))
    else:
        p[0] = ('println', p[3], p.lineno(1))

def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN block elseif_list else_block'''
    p[0] = ('if', p[3], p[5], p[6], p[7], p.lineno(1))

def p_elseif_list(p):
    '''elseif_list : elseif_list elseif
                   | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_elseif(p):
    '''elseif : ELSEIF LPAREN expression RPAREN block'''
    p[0] = ('elseif', p[3], p[5], p.lineno(1))

def p_else_block(p):
    '''else_block : ELSE block
                  | empty'''
    p[0] = p[1]

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = p[2]

def p_function_definition(p):
    '''function_definition : ZAP IDENTIFIER LPAREN parameter_list RPAREN block'''
    p[0] = ('function', p[2], p[4], p[6])

def p_parameter_list(p):
    '''parameter_list : IDENTIFIER
                      | parameter_list COMMA IDENTIFIER
                      | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON'''
    p[0] = ('return', p[2], p.lineno(1))

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                  | IDENTIFIER
                  | TRUE
                  | FALSE
                  | LPAREN expression RPAREN
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression %prec NOT
                  | MINUS expression %prec UMINUS
                  | function_call
                  | anonymous_function'''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('not', p[2], p.lineno(1)) if p[1] == '!' else ('uminus', p[2], p.lineno(1))
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = (p[2], p[1], p[3])

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression
                     | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_lambda_expression(p):
    '''lambda_expression : IDENTIFIER ASSIGN anonymous_function SEMICOLON'''
    p[0] = ('lambda', p[1], p[3], p.lineno(1))

def p_anonymous_function(p):
    '''anonymous_function : LAMBDA LPAREN parameter_list RPAREN COLON LBRACE expression RBRACE'''
    p[0] = ('anonymous', p[3], p[7], p.lineno(1))

def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN argument_list RPAREN'''
    p[0] = ('call', p[1], p[3], p.lineno(1))

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_comment(p):
    '''comment : COMMENT IDENTIFIER'''
    p[0] = None


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
# parser = yacc.yacc(write_tables=False, debug=False)
