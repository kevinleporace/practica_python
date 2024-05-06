class Padre:
    def __init__(self,nombre,apellido,auto):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__auto=auto

    def jugar_futbol(self):
        return 'jugando futbol'
   
    def cocinar(self):
        return 'cocinando'
    
    def __str__(self):
        return f'datos basicos padre: \nnombre: {self.__nombre}\napellido: {self.__apellido}\nauto: {self.__auto}'

class Hijo(Padre):
    def __init__(self,nombre,apellido,auto,motocicleta):
        super().__init__(nombre,apellido,auto)
        self.__motoclicleta=motocicleta
    
    def correr(self):
        return 'corriendo'


padre=Padre('esteban','tribul','si')
print(padre.__str__())

hijo=Hijo('esteban','tribul jr','si','no')
print(hijo.__str__())