import math

class Persona:
    def __init__(self,nombre,apellido,altura,peso):
        self.nombre=nombre
        self.apellido=apellido
        self.altura=altura
        self.peso=peso
    
    def calcular_imc(self):
         imc=self.peso/math.pow(self.altura,2)
         
         return round(imc,2)

class Trabajador(Persona):
    def __init__(self,nombre,apellido,altura,peso):
        Persona.nombre=nombre
        Persona.apellido=apellido
        Persona.altura=altura
        Persona.peso=peso


    
    def trabajar(self):
        return 'estoy trabajando'

class Instituto:
    def __init__(self,nombre_ins):
        self.nombre_ins=nombre_ins
    def estudiando(self):
        return f'estoy estudiando en {self.nombre}'

'''consider al estudiante como un trabajador y trabajador hereda a persona'''  
class Estudiante(Trabajador,Instituto):
    def __init__(self,nombre,apellido,altura,peso,nombre_ins):
        Trabajador.nombre=nombre
        Trabajador.apellido=apellido
        Trabajador.altura=altura
        Trabajador.peso=peso
        Instituto.__init__(self,nombre_ins)
    
    def estudiar(self):
        return  'me gusta estudiar'

estudiante=Estudiante('pablo','escoporti',1.70,100,'marina mercante')
print(estudiante.estudiando())
print(estudiante.calcular_imc())
print(estudiante.nombre)
print(estudiante.estudiando())

