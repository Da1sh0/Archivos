# Especificadores de acceso
class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self._edad = edad  
        self.__direccion = direccion

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self._edad)

# Crear una instancia de la clase Persona
persona1 = Persona("Diiego", 19, "Cra 16B")
# Acceder a los miembros de la clase
print("Nombre:", persona1.nombre)
print("Edad:", persona1._edad)  # Aunque es "protected", se puede acceder (no es una restricción fuerte)
# Acceder a la información a través de un método público
persona1.mostrar_informacion()
# Acceder al atributo '__direccion' de manera indirecta (name mangling)
print("Dirección:", persona1._Persona__direccion)


#Es un mecanismo en Python que realiza una transformación en el nombre de los atributos de clase que comienzan con dos guiones bajos (__). Esta transformación se aplica para evitar colisiones de nombres cuando una clase es heredada y las subclases tienen atributos con el mismo nombre que los atributos de la clase base.
#Cuando se utiliza un doble guion bajo para definir un atributo en una clase, Python lo transforma internamente en un nombre que incluye el nombre de la clase. El patrón utilizado es _<nombre de la clase>__<atributo>.
#Por ejemplo, si tienes una clase Persona con un atributo __direccion, el nombre real del atributo dentro de la clase se convierte en _Persona__direccion. Esto se hace para evitar posibles conflictos de nombres con subclases que también pueden tener un atributo llamado __direccion.