import ply.lex as lex

tokens = (
    'NUMBER',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'AND',
    'OR',
    'NOT',
    'EQ',
    'NEQ',
    'GT',
    'LT',
    'GE',
    'LE',
    'ASSIGN',
    'SEMICOLON',
    'COLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'PRINTLN',
    'PRINT',
    'IF',
    'ELSE',
    'ELSEIF',
    'RETURN',
    'ZAP',
    'TRUE',
    'FALSE',
    'LAMBDA',
    'COMMENT'
)

t_ASSIGN    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MODULO    = r'%'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'
t_EQ        = r'=='
t_NEQ       = r'!='
t_GT        = r'>'
t_LT        = r'<'
t_GE        = r'>='
t_LE        = r'<='
t_SEMICOLON = r';'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_COMMA     = r','
t_COLON     = r'\:'

t_ignore = ' \t'

def t_PRINTLN(t):
    r'println'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ZAP(t):
    r'zap'
    return t

def t_LAMBDA(t):
    r'lambda'
    return t

def t_TRUE(t):
    r'True'
    return t

def t_FALSE(t):
    r'False'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    raise Exception (f"Illegal character '{t.value[0]}', at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
#lexer = lex.lex(debug=False)
