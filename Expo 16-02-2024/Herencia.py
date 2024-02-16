
# Herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"{self.marca} {self.modelo}"

# Crear una instancia de la clase Vehiculo
mi_auto = Vehiculo(marca="Mazda", modelo="CX-30")
# Llamar al método obtener_informacion para obtener la información del vehículo
informacion_auto = mi_auto.obtener_informacion()
# Imprimir la información del vehículo
print(informacion_auto)

