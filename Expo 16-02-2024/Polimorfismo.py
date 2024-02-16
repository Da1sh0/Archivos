# Polimorfismo
def area(figura):
    return figura.calcular_area()

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2

# Ejemplo de uso
cuadrado = Cuadrado(5)
circulo = Circulo(3)
print(area(cuadrado))  # Imprime el área del cuadrado con lado 5
print(area(circulo))   # Imprime el área del círculo con radio 3


