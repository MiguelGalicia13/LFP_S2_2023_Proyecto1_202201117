from Expresiones.expresion import *
import math
class Expresion_Arimetica(Expresion):
    errores ={}
    def __init__ (self,tipo,valor1,valor2,linea,columna):
        self.tipo=tipo
        self.valor1=valor1
        self.valor2=valor2
        self.linea=linea
        self.columna=columna
    def interpretar(self):
        global errores
        valor1=self.valor1
        valor2=self.valor2
        if isinstance(valor1,Expresion):
            valor1=valor1.interpretar()
            print("RESULTADO: ",valor1)
        else:
            valor1=self.valor1
        if isinstance(valor2,Expresion):
            valor2=valor2.interpretar()
            print("RESULTADO: ",valor2)
        else:
            valor2=self.valor2
        print("===================================")
        print("OPERACION: ",self.tipo)
        print("tipo: ", self.tipo)
        print("valor1: ", valor1)
        print("valor2: ", valor2)
        resultado = None
        if self.tipo == "suma":
            resultado = valor1 + valor2
        elif self.tipo == "resta":
            resultado = valor1 - valor2
        elif self.tipo == "multiplicacion":
            resultado = valor1 * valor2
        elif self.tipo == "division":
            if valor2==0:
                errores["Division entre 0"]= "Error en linea: "+str(self.linea)+" columna: "+str(self.columna)
                return 
            resultado = valor1 / valor2
        elif self.tipo == "potencia":
            resultado = math.pow(valor1, valor2)
        elif self.tipo == "raiz":
            resultado = math.pow(valor1, 1 / valor2)
        elif self.tipo =="inverso":
            resultado = 1/valor1
        return round(resultado,2)
    def __str__(self) -> str:
        return (
            super().__str__()
            + " tipo: "
            + self.tipo
            + " valor1: "
            + str(self.valor1)
            + " valor2: "
            + str(self.valor2)
        )
    def devolver_errores(self):
        
        return self.errores
