# -*- coding: UTF-8 -*-

# las funciones se definen usando la palabra clave def
def restodiv(a,b):
    while a >= b:
        a = a - b
    return a

print restodiv(11,5)
print restodiv(100,27)

# podemos retornar más de un valor
def divide(a,b):
    i = 0
    while a >= b:
        a = a - b
        i = i + 1
    return i, a

div,resto = divide(10,3)
print "10/3 = %d y resta %d" % (div,resto)
