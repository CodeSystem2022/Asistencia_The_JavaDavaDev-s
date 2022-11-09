from cuadrado import cuadrado
from rectangulo import rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = cuadrado(8, 'Azul')
cuadrado1.alto = -10
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(cuadrado.mro())

print(cuadrado1)
print('Creación de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = rectangulo(3, 9, 'verde')
rectangulo1.ancho = 15
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)