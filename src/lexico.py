import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'LPAREN', 'RPAREN', 'CHARS'
    # Si necesitas agregar más tokens, puedes hacerlo aquí:
    # 'DIVIDE'  # Por ejemplo, para la división
)

# Reglas de los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_CHARS = r'[a-zA-Z]+'

# Si necesitas agregar más tokens, puedes agregar las reglas aquí.
# Ejemplo de un token para la división:
# t_DIVIDE = r'\/'

# Regla de ignorar espacios en blanco
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

if __name__ == "__main__":
    data = '3 + 4 * (5 - 2)'  # Ejemplo de entrada
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"Tipo de Token: {tok.type}, Valor: {tok.value}")