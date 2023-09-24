from Expresiones.expresion import *
import math
class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    def interpretar(self):
        valor = self.valor
        if isinstance(valor, Expresion):
            valor = valor.interpretarw()
        else:
            valor = self.valor
        print("===================================")
        print("tipo: ", self.tipo)
        print("valor: ", valor)
        resultado = None
        if self.tipo == "seno":
            resultado = math.sin(valor)
        elif self.tipo == "coseno":
            resultado = math.cos(valor)
        elif self.tipo == "tangente":
            if valor ==90:
                return "Error: tangente de 90"
            resultado = math.tan(valor)
        return round(resultado, 2)