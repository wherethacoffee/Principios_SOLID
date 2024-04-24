#El SRP dice que una clase debe tener una sola razón para cambiar. 
#En otras palabras, una clase debe hacer una sola cosa y hacerlo bien.

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

#Codigo que incumple con el principio:
class CalculadoraInc:
    def operacion(self, a, b, operador):
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b 