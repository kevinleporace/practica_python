'''metodo geter se usa para que no se modifique el valor de tal variable
   metodo seter para agregar un valor a esa variable
'''
class Celular:
    def __init__(self):
        self.__pantalla=''
        self.__forma=''
        self.__ram=0
        self.__almacenamiento=0
        self.__camara=0
       

    def get_pantalla(self):
        return self.__pantalla
    def set_pantalla(self,pantalla):
        self.__pantalla=pantalla
        
    def get_forma(self):
        return self.__forma
    def set_forma(self,forma):
        self.__forma=forma
    
    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram=ram
   
    def get_almacenamiento(self):
        return self.__almacenamiento
    def set_almacenamiento(self,almacenamiento):
        self.__almacenamiento=almacenamiento
   
    def get_camara(self):
        return self.__camara
    def set_camara(self,camara):
        self.__camara=camara

samsung=Celular()

samsung.set_pantalla('amoled')
samsung.set_forma('rectangulo')
samsung.set_ram(6)
samsung.set_almacenamiento(128)
samsung.set_camara(48)
print(samsung.get_pantalla())
#-----------------------------------------------------
xiaomi=Celular()
xiaomi.set_pantalla('ats')
xiaomi.set_forma('rectangular')
xiaomi.set_ram(6)
xiaomi.set_almacenamiento(128)
xiaomi.set_camara(48)
print(xiaomi.get_pantalla())
print(xiaomi.get_forma())

print(samsung.get_pantalla())














