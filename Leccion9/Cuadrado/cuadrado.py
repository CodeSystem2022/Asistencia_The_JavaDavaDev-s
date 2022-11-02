from figuraGeometrica import figuraGeometrica
from color import color


class cuadrado(figuraGeometrica, color):
    def __init__(self, lado, color):
        # super.__init__(lado)
        figuraGeometrica.__init__(self, lado, lado)
        color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{figuraGeometrica.__str__(self)} {color.__str__(self)}'