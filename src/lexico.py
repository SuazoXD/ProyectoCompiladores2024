import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'LPAREN', 'RPAREN', 
    'CHARS', 'QUOTE', 'CONCAT', 'IMPRIMIRRESULTADO', 
    'DIVIDE', 'VARIABLE', 'ASSIGN'
)

# Reglas de los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_CHARS = r'[a-zA-Z ]+'  # Permitir letras y espacios
t_QUOTE = r'\''
t_CONCAT = r'&'
t_IMPRIMIRRESULTADO = r'ImprimirResultado'
t_ASSIGN = r'='  # Regla para asignación

# Regla de ignorar espacios en blanco
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

