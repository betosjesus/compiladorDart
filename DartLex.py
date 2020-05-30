# -------------------------
# ExpressionLanguageLex.py
#--------------------------

import ply.lex as lex

reservadas = ['IF', 'ELSE', 'SWITCH', 'CASE', 'DEFAULT', 'BREAK', 
             'FOR', 'DO', 'WHILE', 'INT', 'FLOAT', 'CHAR', 'STRING',
             'VOID', 'TRUE', 'FALSE',
             'NULL', 'CLASS', 'FINAL', 'CONST', 'VAR', 'FUNCTION',
             'RETURN'
            ]

tokens = reservadas + [
       # Literais
         'ID', 'NUMBER', 'INTEGER', 'LITERAL_STRING',
       # Operators (+,-,*,/,%,==,<,>,<=,>=,!=,!,||,&&,++)
         'SOMA', 'SUBTRAIR', 'VEZES', 'DIVIDIR', 'RESTO',
         'IGUAL', 'MENOR', 'MAIOR', 'MENORI', 'MAIORI',
         'NEG', 'NOT', 'OR', 'AND',
         'ATRIBUIR', 'SOMASOMA', 'SUBSUB',
      # Delimitadores ( ) [ ] { } , . ; :
         'LPAREN', 'RPAREN', 'LCON', 'RCON', 'LCHAV', 'RCHAV',
         'COMMA', 'PCOMMA', 'PONTOS'
]

#reservadas = {
#    'abstract':'ABSTRACT',
#    'if':'IF',
#    'else':'ELSE', 
#    'for':'FOR',
#    'while':'WHILE', 
#    'do':'DO', 
#    'return':'RETURN', 
#    'import':'IMPORT'
#}
#tokens = tokens + list(reservadas.values())

# Newlines
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# IgnoreTab
t_ignore = ' \t'

# Operators (++,--,+,-,*,/,%,==,<,>,<=,>=,!=,!,||,&&)
t_SOMASOMA = r'\+\+'
t_SUBSUB = r'\-\-'
t_SOMA = r'\+'
t_SUBTRAIR = r'\-'
t_VEZES = r'\*'
t_DIVIDIR = r'\/'
t_RESTO = r'\%'
t_IGUAL= r'=='
t_MENOR = r'<'
t_MAIOR = r'>'
t_MENORI = r'<='
t_MAIORI = r'>='
t_NEG = r'!='
t_NOT = r'!'
t_OR = r'\|\|'
t_AND = r'&&'
t_ATRIBUIR = r'='

# Delimitadores ( ) [ ] { } , ; :
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCON = r'\['
t_RCON = r'\]'
t_LCHAV = r'\{'
t_RCHAV = r'\}'
t_COMMA = r','
t_PCOMMA = r';'
t_PONTOS = r':'

t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_LITERAL_STRING = r'\"([^\\\n]|(\\.))*?\" | \'([^\\\n]|(\\.))*?\''


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value.upper() in reservadas:
        t.value = t.value
        t.type = t.value.upper()

    return t

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

def  t_COMMENT_MONOLINE(t):
    r'//.*'
    pass

def  t_ccode_comment(t):
   r'(/\*(.|\n)*?\*/) | (//.*)'
   pass

def t_BRANCO(t):
   r'[ \t]'
   pass