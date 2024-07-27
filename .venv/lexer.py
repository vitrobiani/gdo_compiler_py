# lexer.py
import ply.lex as lex

tokens = (
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'SEMI',
    'GT',
    'LT',
    'GE',
    'LE',
    'EQ',
    'IF',
    'ELSE',
    'PRINT',
    'LAMBDA',
    'COLON',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'RETURN',
    'ZAP'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_PRINT = r'print'
t_RETURN = r'return'
t_ZAP = r'zap'

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'lambda': 'LAMBDA',
    'return': 'RETURN',
    'zap': 'ZAP'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
