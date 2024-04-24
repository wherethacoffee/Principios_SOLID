#El OCP dice que las clases deben estar abiertas para extensión 
#pero cerradas para modificación. Esto significa que puedes agregar 
#nuevas funcionalidades sin modificar el código existente.

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio
    
#Código que incumple con el principio
class Forma:
    def __init__(self, tipo):
        self.tipo = tipo

    def area(self):
        if self.tipo == "Rectangulo":
            return self.calcular_area_rectangulo()
        elif self.tipo == "Circulo":
            return self.calcular_area_circulo()

    def calcular_area_rectangulo(self):
        # Cálculo del área del rectángulo
        pass

    def calcular_area_circulo(self):
        # Cálculo del área del círculo
        pass

