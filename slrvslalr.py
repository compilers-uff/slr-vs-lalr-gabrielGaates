from ply import lex
from ply import yacc
import sys

tokens = ('NUMBER','TIMES','EQUALS','NAME','OR')

t_TIMES   = r'\*'
t_EQUALS  = r'='
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = r' '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_error(t):
    print(f"Caracter nao permitido{t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_igual(p):
    '''s : l EQUALS r
                    | r'''

def p_vezes(p):
    '''l : TIMES r
                    | term'''

def p_atribuir(p):
    '''r : l '''


def p_termo(p):
    '''term : NAME
                | NUMBER '''


def p_error(p):
    print("Erro")

compiladores = yacc.yacc(method='SLR')


