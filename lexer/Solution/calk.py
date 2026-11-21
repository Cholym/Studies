

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'T_DoubleConstant','T_IntConstant','T_StringConstant','T_BoolConstant',
    'T_Identifier',
    'T_Void','T_Int','T_Double','T_Bool','T_String','T_Class','T_Interface',
    'T_Null','T_This','T_Extends','T_Implements','T_For','T_While','T_If',
    'T_Else','T_Return','T_Break','T_New','T_NewArray','T_Print',
    'T_ReadInteger','T_ReadLine',
    'T_LE','T_GE','T_Equal','T_NotEqual','T_And','T_Or','T_Dims',
)

literals = '+-*/%<>!=;,.[](){}'

t_T_LE       = r'<='
t_T_GE       = r'>='
t_T_Equal    = r'=='
t_T_NotEqual = r'!='
t_T_And      = r'&&'
t_T_Or       = r'\|\|'
t_T_Dims     = r'\[\]'

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

if __name__=="__main__":
    data = ' 123 + 345 * ( 45 - 33) / 2334 '
    lexer.input(data)
    while True:
        tok = lexer.token() # читаем следующий токен
        if not tok: break      # закончились печеньки
        print ( tok )