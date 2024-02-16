
# Composicion
class Motor:
    def arrancar(self):
        print("Motor arrancado")

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.arrancar()

# Crear una instancia de la clase Coche
mi_coche = Coche()
# Llamar al método arrancar para arrancar el motor
mi_coche.arrancar()

