from productos import Producto

class Orden:
    contador_ordenes=0
    def __init__(self,productos):#lista de productos
        Orden.contador_ordenes+=1
        self._id_orden=Orden.contador_ordenes
        self._productos=list(productos)
    
    def agregar_producto(self,producto):
        self._productos.append(producto)

    #la suma del precio de la orden que recibe una lista con productos
    def calcular_precio_orden(self):
        suma_precio=0
        for p in self._productos:
           suma_precio+=p._precio
       
        return suma_precio
    
    def __str__(self):
        producto_str=''
        for p in self._productos:
            producto_str+=p.__str__() +'\n'
        return f'orden: {self._id_orden} \nproductos:\n{producto_str}'
            



if __name__=='__main__':
    producto1=Producto('procesador i3',500)
    producto2=Producto('procesador i7',750)
    productos_lista=[producto1,producto2]
    orden1=Orden(productos_lista)
    orden1.agregar_producto(Producto('i9',1000))
    print(orden1)
    print('precio total: ',orden1.calcular_precio_orden())
   
   