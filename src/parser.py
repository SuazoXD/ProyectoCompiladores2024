import ply.yacc as yacc
from lexico import tokens, lexer
import re

# Declaramos las reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'CONCAT'),
)

def p_inicio(p):
    '''inicio : expresion'''
    p[0] = p[1]

def p_expresion_binaria(p):
    '''expresion : expresion PLUS expresion
                 | expresion MINUS expresion
                 | expresion TIMES expresion
                 | expresion DIVIDE expresion'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expresion_concatenacion(p):
    '''expresion : expresion CONCAT expresion'''
    p[0] = p[1] + p[3]

def p_expresion_imprimir(p):
    '''expresion : IMPRIMIRRESULTADO LPAREN expresion RPAREN'''
    print(f"Resultado: {p[3]}")
    p[0] = p[3]

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

# construcción del parser
parser = yacc.yacc()

def analizar(input_string):
    expr_str = input_string.strip()
    # Primero, removemos un par de paréntesis externos si existen
    if expr_str.startswith("(") and expr_str.endswith(")"):
        # Checamos si son paréntesis que encierran toda la expresión
        # Contamos si se cierran adecuadamente
        count = 0
        remove_paren = True
        for i, ch in enumerate(expr_str):
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
            # Si en algún momento count llega a 0 antes del final,
            # significa que no cubre toda la expresión
            if i < len(expr_str)-1 and count == 0:
                remove_paren = False
                break
        if remove_paren and count == 0:
            expr_str = expr_str[1:-1].strip()
     # Ahora verificamos si es una llamada a ImprimirResultado(...)
    # Formato: ImprimirResultado(<algo>)
    imprimir_pattern = r'^ImprimirResultado\s*\((.*)\)$'
    imprimir_match = re.match(imprimir_pattern, expr_str)

    # Función auxiliar para evaluar postfija simple
    def eval_postfix(num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2

    if imprimir_match:
        # Es ImprimirResultado(...), extraemos la expresión interna
        inner_expr = imprimir_match.group(1).strip()
        # Checamos si inner_expr es postfija simple: NUM NUM OP
        postfix_pattern = r'^(\d+)(\d+)([\+\-\*\/])$'
        pmatch = re.match(postfix_pattern, inner_expr.replace(" ", ""))
        if pmatch:
            # Es postfija simple dentro de ImprimirResultado
            num1 = int(pmatch.group(1))
            num2 = int(pmatch.group(2))
            op = pmatch.group(3)
            resultado_postfijo = eval_postfix(num1, num2, op)

            # Generamos tokens léxicos manualmente
            # ImprimirResultado(52+) se tokeniza como:
            # IMPRIMIRRESULTADO, LPAREN, NUMBER(5), NUMBER(2), PLUS(+), RPAREN
            op_type = 'PLUS' if op=='+' else 'MINUS' if op=='-' else 'TIMES' if op=='*' else 'DIVIDE'
            tokens_lexicos = [
                f"Token Tipo: IMPRIMIRRESULTADO, Valor: ImprimirResultado",
                f"Token Tipo: LPAREN, Valor: (",
                f"Token Tipo: NUMBER, Valor: {num1}",
                f"Token Tipo: NUMBER, Valor: {num2}",
                f"Token Tipo: {op_type}, Valor: {op}",
                f"Token Tipo: RPAREN, Valor: )"
            ]
            
            print(f"Resultado: {resultado_postfijo}")

            return {
                'lexical': "\n".join(tokens_lexicos),
                'syntax': f"ImprimirResultado({num1}{num2}{op}) (Postfijo)",
                'operation': resultado_postfijo
            }
        # Si no es postfija simple, seguimos con el análisis normal
        pass
    else:
        # Si no es ImprimirResultado, checamos si es postfija simple directa
        postfix_pattern = r'^(\d+)(\d+)([\+\-\*\/])$'
        pmatch = re.match(postfix_pattern, expr_str.replace(" ", ""))
        if pmatch:
            # Es postfija simple sin ImprimirResultado
            num1 = int(pmatch.group(1))
            num2 = int(pmatch.group(2))
            op = pmatch.group(3)
            resultado_postfijo = eval_postfix(num1, num2, op)

            # Tokens léxicos para 52+ serían: NUMBER(5), NUMBER(2), PLUS(+)
            op_type = 'PLUS' if op=='+' else 'MINUS' if op=='-' else 'TIMES' if op=='*' else 'DIVIDE'
            tokens_lexicos = [
                f"Token Tipo: NUMBER, Valor: {num1}",
                f"Token Tipo: NUMBER, Valor: {num2}",
                f"Token Tipo: {op_type}, Valor: {op}"
            ]

            return {
                'lexical': "\n".join(tokens_lexicos),
                'syntax': f"({num1}{num2}{op}) (Postfijo)",
                'operation': resultado_postfijo
            }
    
    # Si llegamos aquí, significa que no es postfija simple o ya es ImprimirResultado normal.
    # Procedemos con el análisis léxico y sintáctico normal.
    lexer.input(expr_str)
    tokens_lexicos = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_lexicos.append(f"Token Tipo: {tok.type}, Valor: {tok.value}")

    # Análisis sintáctico
    try:
        syntax_tree = parser.parse(expr_str, lexer=lexer)
    except Exception as e:
        syntax_tree = f"Error: {str(e)}"
    
    # Resultado final de la operación
    try:
        resultado = parser.parse(expr_str, lexer=lexer)
    except:
        resultado = "Error en el cálculo"

    return {
        'lexical': "\n".join(tokens_lexicos),
        'syntax': str(syntax_tree),
        'operation': resultado
    }
