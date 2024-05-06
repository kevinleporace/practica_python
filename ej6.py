class Vehiculo:
    def __init__(self,color,ruedas):
        self._color=color
        self._ruedas=ruedas
    
    def __str__(self):
        return f'color: {self._color}, ruedas: {self._ruedas}'

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self._velocidad=velocidad
    
    def __str__(self):
        return f'{super().__str__()}, velocidad: {self._velocidad}km/h'
    

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self._tipo=tipo
    
    def __str__(self):
        return f'{super().__str__()}, tipo: {self._tipo}'
    
vehiculo1=Vehiculo('rojo',4)
print(vehiculo1)

ferrari=Coche('amarillo',4,245)
print(ferrari)

biciBacana=Bicicleta('azul',2,'montaña')
print(biciBacana)