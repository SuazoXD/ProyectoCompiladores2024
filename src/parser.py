import ply.yacc as yacc
from lexico import tokens, lexer

variables = {}

# Declaramos las reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES'),
    ('left', 'CONCAT'),  # Agregar precedencia para concatenación
)

def p_inicio(p):
    '''inicio : expresion
              | inicio expresion'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]  # El resultado final será el último valor evaluado.


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
        
def p_asignacion(p):
    '''expresion : ID ASSIGN expresion'''
    variables[p[1]] = p[3]
    p[0] = p[3]
    print(f"Variable '{p[1]}' asignada a {p[3]}")
    print(variables)


def p_expresion_imprimir(p):
    '''expresion : IMPRIMIRRESULTADO LPAREN expresion RPAREN'''
    print(f"Resultado: {p[3]}")  # Imprime el resultado.
    p[0] = p[3]  # Devuelve el valor de la expresión. 
    
def p_expresion_concat(p):
    '''expresion : CONCAT LPAREN lista_expresiones RPAREN'''
    # Concatenamos las expresiones, eliminando las comillas si es una cadena
    p[0] = ''.join(map(lambda x: str(x).strip('"'), p[3]))  # Eliminamos las comillas
    print(f"Concatenación: {p[0]}")

def p_lista_expresiones(p):
    '''lista_expresiones : expresion
                         | lista_expresiones COMA expresion'''
    if len(p) == 2:
        p[0] = [p[1]]  # Si solo hay una expresión
    else:
        p[0] = p[1] + [p[3]]  # Concatenar las expresiones separadas por coma


def p_expresion_variable(p):
    '''expresion : ID'''
    if p[1] in variables:
        p[0] = variables[p[1]]  # Usar el valor de la variable definida
    else:
        raise Exception(f"Error: la variable '{p[1]}' no está definida.")

def p_expresion_cadena(p):
    '''expresion : QUOTE CHARS QUOTE'''
    p[0] = p[2]  # Usar el texto entre comillas


def p_expresion_numero(p):
    'expresion : NUMBER'
    p[0] = int(p[1])

def p_expresion_parentesis(p):
    'expresion : LPAREN expresion RPAREN'
    p[0] = p[2]
    

def p_repeat(p):
    '''expresion : CHARS'''
    p[0] = str(p[1])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

#construcción del parser
parser = yacc.yacc()
def analizar(input_string):
    # Análisis léxico y almacenamiento de tokens
    lexer.input(input_string)
    tokens_lexicos = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_lexicos.append(f"Token Tipo: {tok.type}, Valor: {tok.value}")
    
    # Análisis sintáctico y cálculo del resultado
    try:
        resultado = parser.parse(input_string, lexer=lexer)
        syntax_tree = resultado  # Representa el árbol o resultado del análisis sintáctico
    except Exception as e:
        syntax_tree = f"Error de sintaxis: {str(e)}"
        resultado = None

    # Devolvemos los resultados detallados
    return {
        'lexical': "\n".join(tokens_lexicos),  # Detalle del análisis léxico
        'syntax': syntax_tree,  # Árbol sintáctico o mensaje de error
        'operation': resultado  # Resultado final del cálculo
    }