
# Agregacion
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear instancias de las clases Departamento y Empleado
departamento_ventas = Departamento(nombre="Ventas")
empleado1 = Empleado(nombre="Diiego")
empleado2 = Empleado(nombre="Luiisa")
# Agregar empleados al departamento
departamento_ventas.empleados.append(empleado1)
departamento_ventas.empleados.append(empleado2)
# Imprimir información del departamento y empleados
print("Nombre del Departamento: ",departamento_ventas.nombre)
print("Lista de Empleados:")
for empleado in departamento_ventas.empleados:
    print("- ",empleado.nombre,"")

