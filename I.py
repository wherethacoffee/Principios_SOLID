#El ISP sostiene que una clase no debe verse obligada 
#a implementar interfaces que no utiliza. Divide las interfaces 
#en interfaces más pequeñas y específicas.
class ITrabajo:
    def trabajar(self):
        pass

class IComer:
    def comer(self):
        pass

class Persona(ITrabajo, IComer):
    def trabajar(self):
        print("La persona trabaja duro")

    def comer(self):
        print("La persona come saludablemente")

#Código que incumple con el principio
class IActividades:
    def trabajar(self):
        pass

    def comer(self):
        pass

class Persona(IActividades):
    def trabajar(self):
        print("La persona trabaja duro")

    def comer(self):
        print("La persona come saludablemente")

