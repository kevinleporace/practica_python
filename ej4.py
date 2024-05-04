
class Celular:
    def __init__(self):
        self.__pantalla=''
        self.__forma=''
        self.__ram=0
        self.__almacenamiento=0
        self.__camara=0
        self.__encendido=False
       
#--------------------metodos geter y seter-------------------------
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
    
    def get_encendido(self):
        return self.__encendido

#------------metodos de clases------------------
    def encender(self):
        print('Encendiendo el celular')
        self.__encendido=True
    def apagar(self):
        print('Apagando el celular')
        self.__encendido=False
    
    def __str__(self):
        return f'\npantalla ->{samsung.__pantalla}\nalmacenamiento ->{samsung.__almacenamiento}'
    

samsung=Celular()

samsung.set_pantalla('ipc')
samsung.set_forma('curva')
samsung.set_ram(8)
samsung.set_almacenamiento(256)
samsung.set_camara(64)
print(samsung.__str__())

if (samsung.get_encendido()):
    print('hola')
else:
    print('el celular esta apagado')














