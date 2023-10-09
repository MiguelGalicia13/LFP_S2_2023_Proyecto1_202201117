from collections import namedtuple
from Expresiones import *
from Expresiones.arimeticas import Expresion_Arimetica
from Expresiones.trigonometricas import ExpresionTrigonometrica
Token = namedtuple("Token", ["value", "line", "col"])

# numero de linea
line = 1
# numero de columna
col = 1

tokens = []
errores = []


configuracion = {
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}
# formar un string
def tokenize_string(input_str, i):
    token = ""
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("Error: string no cerrado")


# formar un numero
def tokenize_number(input_str, i):
    token = ""
    isDecimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == "." and not isDecimal:
            token += char
            i += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(token), i]
    return [int(token), i]


#? Gereacion de tokens
def tokenize_input(input_str):
    global line, col, tokens
    #? itera el input
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char.isspace(): #? Si es espacio sangria o salt ode linea
            #?Salto de Linea
            if char == "\n":
                print({"char": char, "line": line, "col": col, "i": i})
                line += 1
                col = 1
            #? Identacion
            elif char == "\t":
                col += 4
            #? Espacio
            else:
                col += 1
            i += 1
        #?Forma un token si es string
        elif char == '"':
            string, pos = tokenize_string(input_str[i + 1 :], i)
            col += len(string) + 1
            i = pos + 2
            token = Token(string, line, col)
            tokens.append(token)
        elif char in ["{", "}", "[", "]", ",", ":"]:
            print({"char": char, "line": line, "col": col, "i": i})
            col += 1
            i += 1
            token = Token(char, line, col)
            tokens.append(token)
        #? si es un digito
        elif char.isdigit():
            number, pos = tokenize_number(input_str[i:], i)
            col += pos - i
            i = pos
            token = Token(number, line, col)
            tokens.append(token)
        else:
            print(
                "Error: caracter desconocido:",
                char,
                "en linea:",
                line + 1,
                "columna:",
                col + 1,
            )
            i += 1
            col += 1


# ?crear las instrucciones a partir de los tokens
def get_instruccion():
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        print("VALUE: ", token)
        if token.value == "operacion":
            # eliminar el :
            tokens.pop(0)
            operacion = tokens.pop(0).value
        elif token.value == "valor1":
            # eliminar el :
            tokens.pop(0)
            value1 = tokens.pop(0).value
            if value1 == "[":
                value1 = get_instruccion()
        elif token.value == "valor2":
            # eliminar el :
            tokens.pop(0)
            value2 = tokens.pop(0).value
            if value2 == "[":
                value2 = get_instruccion()
        elif token.value in ["texto", "fondo", "fuente", "forma"]:
            tokens.pop(0)
            configuracion[token.value] = tokens.pop(0).value
        else:
            print("\033[1;31;40m Error: token desconocido:", token, "\033[0m")
        if operacion and value1 and value2:
            return Expresion_Arimetica(operacion, value1, value2, 0, 0)
        if operacion and operacion in ["seno"] and value1:
            return ExpresionTrigonometrica(operacion, value1, 0, 0)
    return None
#entrada = open("C:\LABS\LFP\LFP_S2_2023_Proyecto1_202201117\prueba.json", "r").read()
def create_instructions():
    global tokens
    instrucciones = []
    while tokens:
        instruccion = get_instruccion()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones
def analizar(entrada):
    tokenize_input(entrada)
    instrucciones = create_instructions()
    for i in instrucciones:
        print("RESULTADO INSTRUCCION: ", i.interpretar())

def errores():
    global errores
    
    return Expresion_Arimetica.devolver_errores()
