from figura import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        FiguraGeometrica.__init__(self,ancho,alto)
    
    def calcular_area(self):
        area=round((self._ancho*self._alto)/2,2)
        return area

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}'