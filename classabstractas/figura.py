from abc import ABC,abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
       
        '''todas las figuras tienen alto y ancho'''
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            self._ancho=0
            print('error no hay figuras negativas')
        if self._validar_valor(alto):
            self._alto=alto
        else:
            self._alto=0
            print('error las figuras no pueden tener valor negativo')
    
    def set_ancho(self,ancho):
        self._ancho=ancho
    def get_ancho(self):
        return self._ancho
    
    def set_alto(self,alto):
        self._alto=alto
    def get_alto(self):
        return self._alto
    
    def _validar_valor(self,valor):
        return True if valor >=0 else False
    
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f'figura geometrica [ancho:{self._ancho} , alto: {self._alto}]'