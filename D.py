#El DIP plantea que los módulos de alto nivel no deben depender 
#de módulos de bajo nivel, ambos deben depender de abstracciones. 
#Además, las abstracciones no deben depender de los detalles, 
#los detalles deben depender de las abstracciones.
class Interruptor:
    def __init__(self, dispositivo):
        self._dispositivo = dispositivo

    def encender(self):
        self._dispositivo.encender()

    def apagar(self):
        self._dispositivo.apagar()

class Luz:
    def encender(self):
        print("Luz encendida")

    def apagar(self):
        print("Luz apagada")


#Código que incumple con el principio
class Interruptor:
    def __init__(self, dispositivo):
        self._dispositivo = dispositivo

    def encender(self):
        if isinstance(self._dispositivo, Luz):
            self._dispositivo.encender()
        elif isinstance(self._dispositivo, Alarma):
            self._dispositivo.activar()

class Alarma:
    def activar(self):
        print("Alarma activada")

