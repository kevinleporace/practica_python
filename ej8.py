class Madre:
    def __init__(self,nombre,apellido,lote):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__lote=lote
   
    def get_lote(self):
        return 'lote',self.__lote

    def jugar_volei(self):
        return 'jugando volei'
    
    def ayudar(self):
        return 'ayudando a las personas'
    
    def __str__(self):
        return f'datos basicos madre: \nnombre: {self.__nombre}\napellido: {self.__apellido}\nlote: {self.__lote}'

class Padre:
    def __init__(self,nombre,apellido,auto):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__auto=auto
    
    def get_auto(self):
        return 'auto',self.__auto

    def jugar_futbol(self):
        return 'jugando futbol'
   
    def cocinar(self):
        return 'cocinando'
    
    
    
    def __str__(self):
        return f'datos basicos padre: \nnombre: {self.__nombre}\napellido: {self.__apellido}\nauto: {self.__auto}'

class Hijo(Padre,Madre):
    def __init__(self,nombre,apellido,auto,lote):
        Padre.__init__(self,nombre,apellido,auto)
        Madre.__init__(self,nombre,apellido,lote)
    
    def correr(self):
        return 'corriendo'

class Nieto(Hijo):
    def __init__(self,nombre,apellido,auto,lote):
        super().__init__(nombre,apellido,auto,lote)

    
   



madre=Madre('mar','leslis',3)
print(madre.__str__())
print(madre.jugar_volei())
print(madre.ayudar())
print()

padre=Padre('esteban','tribul','si')
print(padre.__str__())
print(padre.cocinar())
print(padre.jugar_futbol())
print()

hijo=Hijo('esteban','tribul jr','si',2)
print(hijo.correr())
print(hijo.ayudar())
print(hijo.get_lote())
print(hijo.get_auto())
print(hijo.jugar_futbol())
print()

nieto=Nieto('pedrito','tribul jr','si',2)
print(nieto.correr())
print(nieto.ayudar())
print(nieto.get_lote())
print(nieto.get_auto())
print(nieto.jugar_futbol())

