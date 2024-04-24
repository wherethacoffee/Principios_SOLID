#El LSP establece que los objetos de una clase derivada 
#deben ser capaces de sustituir a los objetos de la clase 
#base sin afectar la corrección del programa.
class Ave:
    def volar(self):
        pass

class Pato(Ave):
    def volar(self):
        print("Un pato vuela con alas")

class Pinguino(Ave):
    def volar(self):
        print("Un pingüino no puede volar, nada en el agua en su lugar")

#Código que incumple con el principio
class Ave:
    def volar(self):
        pass

class Pato(Ave):
    def volar(self):
        print("Un pato vuela con alas")

class Pinguino(Ave):
    def volar(self):
        # Este método no debería lanzar una excepción, como en este caso.
        raise Exception("Un pingüino no puede volar")

