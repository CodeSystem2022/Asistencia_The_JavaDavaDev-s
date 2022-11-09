from color import color
from figuraGeometrica import figuraGeometrica


class rectangulo(figuraGeometrica, color):
    def __init__(self, ancho, alto, color):
        figuraGeometrica.__init__(self, ancho, alto)
        color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{figuraGeometrica.__str__(self)} {color.__str__(self)}'