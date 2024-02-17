import random

# Generar una lista de números aleatorios entre 0 y 100 que sean múltiplos de 11

multiplos = [random.randint(0, 100) * 11 for _ in range(10)]
print(multiplos)
