class Animal:
    def __init__(self,peso,altura,alimentos):
        self._peso=peso
        self._altura=altura
        self._alimentos=alimentos
    
    def set_peso(self,peso):
        self._peso=peso
    def get_peso(self):
        return self._peso
    
    def set_altura(self,altura):
        self._altura=altura
    def get_altura(self):
        return self._altura
    
    def set_alimentos(self,alimentos):
        self._alimentos=alimentos
    def get_alimentos(self):
        return self._alimentos

    def get_imc(self):
        imc=self._peso/(self._altura * self._altura)
        return round(imc,2)
    



# animal1=Animal(50,1.10,['comida1','comida2'])
# print(animal1.get_peso())
# print(animal1.get_altura())
# print(animal1.get_alimentos())
# print(animal1.get_imc())