import time 


def decoracion(funcion):
    def param(*args,**kwargs):
        tiempo1=time.time() 

        resul=funcion(*args,**kwargs)
       
        tiempo2=time.time()
        tiempo_resul=tiempo2-tiempo1
       
        print('la funcion tardo ',tiempo_resul,'segundos')
        return resul
    return param

@decoracion
def division(a,b):
    return f'resultado de la division {a} dividido {b} = {a/b}'


print(division(5,5))