import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'LPAREN', 'RPAREN', 'CHARS', 'QUOTE', 'CONCAT', 'IMPRIMIRRESULTADO', 'ASSIGN', 'ID',
    'COMA', 'DIVIDE'
)

# Reglas de los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_CHARS = r'\"[^\"]*\"'  # Palabras con letras y posibles espacios
t_QUOTE = r'\''
t_CONCAT = r'\'CONCAT\''
t_IMPRIMIRRESULTADO = r"\'ImprimirResultado\'"
t_ASSIGN = r'='
t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_COMA = r','

t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Código de prueba
if __name__ == "__main__":

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Tipo de Token: {tok.type}, Valor: {tok.value}")