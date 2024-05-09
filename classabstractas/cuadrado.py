from figura import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, ancho, alto):
        FiguraGeometrica.__init__(self,ancho,alto)
       
    
    def calcular_area(self):
        if(self._ancho==self._alto):
            return self._ancho*self._alto
        else:
            print('los cuadrados tienen el mism ancho que el alto')
    
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} '