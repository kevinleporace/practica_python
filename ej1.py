'''repaso simple decoradores'''
def decoracion(funcion):
    def param(a,b):
        c=funcion(a,b)
        return c
    return param



@decoracion
def suma(a,b):
    print('funcion suma')
    return a+b

@decoracion
def resta(a,b):
    print('funcion resta')
    return a-b

print(suma(9,8))
print(resta(9,8))
