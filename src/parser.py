import ply.yacc as yacc
from lexico import tokens, lexer

# Declaramos las reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES'),
)

def p_inicio(p):
    '''inicio : expresion'''
    p[0] = p[1]

def p_expresion_binaria(p):
    '''expresion : expresion PLUS expresion
                | expresion MINUS expresion
                | expresion TIMES expresion'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]

def p_expresion_numero(p):
    'expresion : NUMBER'
    p[0] = int(p[1])

def p_expresion_parentesis(p):
    'expresion : LPAREN expresion RPAREN'
    p[0] = p[2]
    
def p_expresion_repeat(p):
    '''expresion : QUOTE expresion QUOTE'''
    p[0] = str(p[2])

def p_repeat(p):
    'expresion : CHARS'
    p[0] = str(p[1])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

parser = yacc.yacc()

def analizar(input_string):
    # Análisis léxico
    lexer.input(input_string)
    tokens_lexicos = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_lexicos.append(f"Token Tipo: {tok.type}, Valor: {tok.value}")
    
    # Análisis sintáctico
    try:
        syntax_tree = parser.parse(input_string, lexer=lexer)
    except Exception as e:
        syntax_tree = f"Error: {str(e)}"
    
    # Resultado final de la operación
    try:
        resultado = parser.parse(input_string, lexer=lexer)
    except:
        resultado = "Error en el cálculo"

    # Devolvemos los resultados detallados
    return {
        'lexical': "\n".join(tokens_lexicos),
        'syntax': str(syntax_tree),  # Mostrar el árbol sintáctico
        'operation': resultado
    }
