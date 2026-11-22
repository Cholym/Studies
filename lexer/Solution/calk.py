

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

# числовые константы и преобразование значений
def t_T_DoubleConstant(t):
    r'\d+\.\d*([eE][+-]?\d+)?'
    t.lexeme = t.value
    t.value  = float(t.value)
    return t

def t_T_IntConstant(t):
    r'0[xX][0-9a-fA-F]+|\d+'
    t.lexeme = t.value
    if t.value[:2].lower() == '0x':
        t.value = int(t.value, 16)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    # t.lexer.line_start = t.lexpos + len(t.value[0]) исправлено, что изменения проявлялись на однострочной строке
    t.lexer.line_start = t.lexpos + len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

VALUE_TOKENS = {'T_IntConstant', 'T_DoubleConstant',
                'T_StringConstant', 'T_BoolConstant'}

# добавлен словарь для render
_VALUE = {
    'T_IntConstant':    lambda v: "%d" % v,
    'T_DoubleConstant': lambda v: "%g" % v,
    'T_StringConstant': lambda v: v,
    'T_BoolConstant':   lambda v: v,
}

# сравнивает вывод
def render(tok):
    lexeme   = tok.lexeme if hasattr(tok, 'lexeme') else tok.value
    type_str = "'%s'" % tok.type if len(tok.type) == 1 else tok.type
    fmt      = _VALUE.get(tok.type)
    value_part = "(value = %s)" % fmt(tok.value) if fmt else ""
    c1 = tok.lexpos - getattr(lexer, 'line_start', 0) + 1
    c2 = c1 + len(lexeme) - 1
    print("%-13s line %d cols %d-%d is %s %s"
          % (lexeme, tok.lineno, c1, c2, type_str, value_part))
    
if __name__=="__main__":
    # data = '+ [] <= != ;'
    data = '0 001 0x0 0X12aE 0x1AeF 12. .12 12.E+2 3.1415E+3 12e5 8'

    lexer.input(data)
    lexer.line_start = 0

    while True:
        tok = lexer.token() # читаем следующий токен
        if not tok: break      # закончились печеньки
        # print ( tok )
        render ( tok )