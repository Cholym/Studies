import io
import os
import sys
from contextlib import redirect_stdout

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
    'T_LessEqual','T_GreaterEqual','T_Equal','T_NotEqual','T_And','T_Or','T_Dims',
)

reserved = {
    'void': 'T_Void', 'int': 'T_Int', 'double': 'T_Double', 'bool': 'T_Bool',
    'string': 'T_String', 'class': 'T_Class', 'interface': 'T_Interface',
    'null': 'T_Null', 'this': 'T_This', 'extends': 'T_Extends',
    'implements': 'T_Implements', 'for': 'T_For', 'while': 'T_While',
    'if': 'T_If', 'else': 'T_Else', 'return': 'T_Return', 'break': 'T_Break',
    'new': 'T_New', 'NewArray': 'T_NewArray', 'Print': 'T_Print',
    'ReadInteger': 'T_ReadInteger', 'ReadLine': 'T_ReadLine',
    'true': 'T_BoolConstant', 'false': 'T_BoolConstant',
}

literals = '+-*/%<>!=;,.[](){}'

t_T_LessEqual    = r'<='
t_T_GreaterEqual = r'>='
t_T_Equal        = r'=='
t_T_NotEqual     = r'!='
t_T_And          = r'&&'
t_T_Or           = r'\|\|'
t_T_Dims         = r'\[\]'

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

def t_T_StringConstant(t):
    r'"[^"\n]*"'
    t.lexeme = t.value
    return t

def t_T_Identifier(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.lexeme = t.value
    if len(t.value) > 31:
        print()
        print(f"*** Error line {t.lineno}.")
        print(f'*** Identifier too long: "{t.value}"')
        print()
        t.type = 'T_Identifier'
        t._truncated = True  # флаг для render
        return t
    t.type = reserved.get(t.value, 'T_Identifier')
    return t

def t_T_StringUnterminated(t):
    r'"[^"\n]*'
    print()
    print(f"*** Error line {t.lineno}.")
    print(f'*** Unterminated string constant: {t.value}')
    print()
    t.lexer.lineno += 1
    t.lexer.line_start = t.lexpos + len(t.value) + 1
    t.lexer.skip(1)  # пропускаем только \n
    return None

def t_COMMENT_SINGLE(t):
    r'//[^\n]*'
    pass

def t_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_COMMENT_UNTERMINATED(t):
    r'/\*(.|\n)*'
    t.lexer.lineno += t.value.count('\n')
    print()  # Пустая строка перед Error
    print(f"*** Error line {t.lineno}.")
    print("*** Unterminated block comment")
    print()  # Пустая строка после Unterminated
    t.lexer.skip(len(t.value))
    return None
t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    # t.lexer.line_start = t.lexpos + len(t.value[0]) исправлено, что изменения проявлялись на однострочной строке
    t.lexer.line_start = t.lexpos + len(t.value)

def t_error(t):
    print()  # Пустая строка перед Error
    print(f"*** Error line {t.lineno}.")
    print(f"*** Unrecognized char: '{t.value[0]}'")
    print()  # Пустая строка после Unrecognized
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
    lexeme = tok.lexeme if hasattr(tok, 'lexeme') else tok.value
    type_str = "'%s'" % tok.type if len(tok.type) == 1 else tok.type
    fmt = _VALUE.get(tok.type)
    value_part = "(value = %s)" % fmt(tok.value) if fmt else ""
    c1 = tok.lexpos - getattr(lexer, 'line_start', 0) + 1
    c2 = c1 + len(lexeme) - 1
    
    formatted_lexeme = "%-13s" % lexeme
    if len(lexeme) >= 13:
        formatted_lexeme += " "
    
    truncated_part = ""
    if getattr(tok, '_truncated', False):
        truncated_part = " (truncated to %s)" % lexeme[:31]
    
    # Три ветки: есть value_part, есть truncated, или ни того ни другого
    if value_part:
        return "%sline %d cols %d-%d is %s %s%s" % (formatted_lexeme, tok.lineno, c1, c2, type_str, value_part, truncated_part)
    elif truncated_part:
        return "%sline %d cols %d-%d is %s%s" % (formatted_lexeme, tok.lineno, c1, c2, type_str, truncated_part)
    else:
        return "%sline %d cols %d-%d is %s " % (formatted_lexeme, tok.lineno, c1, c2, type_str)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calk.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: file '{filename}' not found")
        sys.exit(1)

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    # Перехватываем stdout для сравнения
    f_out = io.StringIO()
    with redirect_stdout(f_out):
        lexer.input(data)
        lexer.line_start = 0
        while True:
            tok = lexer.token()
            if not tok: break
            line = render(tok)
            if line:
                print(line)

    actual = f_out.getvalue()

    # Сравниваем с .out
    base = os.path.splitext(filename)[0]
    out_file = base + '.out'

    if os.path.exists(out_file):
        with open(out_file, 'r', encoding='utf-8') as f:
            expected = f.read()

        if actual == expected:
            print(f"✅ OK: {filename} идентичен {out_file}")
        else:
            print(f"❌ РАСХОЖДЕНИЕ: {filename} vs {out_file}")
            act_lines = actual.split('\n')
            exp_lines = expected.split('\n')
            
            # Показываем ВСЕ различия
            max_lines = max(len(act_lines), len(exp_lines))
            for i in range(max_lines):
                a = act_lines[i] if i < len(act_lines) else "<отсутствует>"
                e = exp_lines[i] if i < len(exp_lines) else "<отсутствует>"
                if a != e:
                    print(f"  Строка {i+1}:")
                    print(f"    Ожидалось: {repr(e)}")
                    print(f"    Получено:  {repr(a)}")
    else:
        print(actual)