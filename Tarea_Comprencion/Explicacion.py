#  forma concisa y eficiente de crear listas.
# nueva_lista = [expresion for elemento in iterable]
# expresion es la expresión que define el valor de cada elemento en la nueva lista.
# elemento es la variable que toma cada valor del iterable.
# iterable es la secuencia de valores sobre la cual iterar.

cuadrados = [x-5 for x in range(11)]
print(cuadrados)

cuadrados_pares = [x+3 for x in range(10) if x % 2 == 0]
print(cuadrados_pares)

