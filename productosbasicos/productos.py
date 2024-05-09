class Producto:
    contador_productos=0
    def __init__(self,nombre,precio):
        Producto.contador_productos+=1
        self._id_producto=self.contador_productos
        self._nombre=nombre
        self._precio=precio
    
    @property
    def get_precio(self):
        return self._precio

    def __str__(self):
        return f'id producto: {self._id_producto} nombre: {self._nombre} precio: {self._precio}'

if __name__=='__main__':
    # producto1=Producto('procesador',1000)
    # print(producto1)

    # producto2=Producto('tarjeta grafica',1700)
    # print(producto2)
    pass