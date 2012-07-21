# -*- coding: UTF-8 -*-

# las excepciones en python funcionan similar a java o c++
# se pueden capturar indicando qué tipo esperamos o no
try:
    # acá hacemos las operaciones
    pass
except:
    # acá cae si ocurre cualquier excepción
    pass
finally:
    # esto se ejecuta haya o no haya excepción
    pass
    
# supongamos vamos a recibir dos numeros y queremos
# dividir uno entre otro. Si el divisor es 0 entonces
# la división no está definida y obtendremos una excepción
try:
    a = input('a: ')
    b = input('b: ')
    print a/b
except:
    print 'error dividiendo'

# podemos ser más explicitos capturando exactamente ZeroDivisionError
try:
    a = input('a: ')
    b = input('b: ')
    print a/b
except ZeroDivisionError as zde:
    print 'error dividiendo --> ',zde


# para lanza excepciones usamos la instrucción raise seguida del
# objeto que la representa
import math

class NegativoError(Exception): pass

def raiz(x):
    if x<0:
        raise NegativoError()
    else:
        return math.sqrt(x)

try:
    print raiz(-1)
except NegativoError:
    print "ups!"

