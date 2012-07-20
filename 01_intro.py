# -*- coding: UTF-8 -*-
# eso ahi arriba declara la codificación de caracteres

# comenzamos con un comentario
# simplemente debe iniciar con #

# python fue creado por Guido van Rossum finales de los 80's
# hoy día sigue dictando la dirección del proyecto

# son varios los paradigmas soportados como programación orientada
# a objetos, programación estructurada, programación funcional y
# programación orientada a aspectos

# todos los tipos de datos son verificados dinámicamente
x=1                        # así tenemos x de tipo entero
x="hola"                   # así sería tipo string
x=10.2                     # así tipo flotante
x=[1,3,"p"]                # una lista
x=(1.5, 'vaya', 44, [1,3]) # una tupla (como listas pero solo lectura)

# para imprimir en la consola usamos la función print
print "hola mundo"
x,n = 10,"jorge" # asignación múltiple
print "es %d y el nombre es %s" % (x,n) # interpolacióno valores en strings

# condicionales con if
x=input("ingrese un número: ")
if x>0:
    print 'es positivo'
elif x==0:
    print 'es 0'
else:                   # la parte else es opcional
    print 'es negativo'

# note que no hay "begin end" ni llaves que marquen los bloques
# la identación es quien dice el inicio y fin

# vamos con ciclos
# range(10) genera una lista de los números del 0 al 9
for i in range(10):
    print i 

# es la misma sintaxis para otras listas
nombres = ['Alicia','Jorge','Luis','Maria']
for n in nombres:
    print n

# también tenemos el while muy parecido a otros lenguajes
# implementamos el resto de la división entera
dividendo = 10
divisor = 3
resto = dividendo
while resto >= divisor:
    resto = resto - divisor
print 'el resto de la división entre %d y %d es %d' % (dividendo,divisor,resto)

