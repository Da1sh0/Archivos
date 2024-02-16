# Encapsulamiento
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_nombre(self):
        return self.__nombre

# Crear una instancia de la clase Persona
persona = Persona(nombre="Diiego", edad=19)
# Obtener y imprimir el nombre de la persona
nombre_persona = persona.obtener_nombre()
print("Nombre de la persona: ",nombre_persona)
