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

# los parámetros pueden tener valores por defecto en caso
# de ser omitidos. Sólo los "ultimos" pueden ser omitidos
def divide2(a,b=1):
    while a >= b:
        a = a - b
    return a

print divide2(5)   # acá b = 1
print divide2(6,2) # igual podemos especificarlo

# las funciones se pueden manipular como un dato cualquiera
f = divide
i,a = f(11,2)

# las podemos pasar por parámetros
def duplica(x):
    return x*x

def aplica(f,lista):
    for i in range(len(lista)):
        lista[i]=f(lista[i])

lista=[1,2,3,4]
aplica(f,lista)    # los cambios son aplicados a la lista
print lista

# se pueden definir expresiones cortas 
# con lambda
lista=[1,2,3,4]
aplica(lambda x: x*x,lista)
print lista

# Las expresiones lambda permiten definir una función corta
# que pueda ser escrita como una sola expresión.
lista=[1,2,3,4]
ff = lambda ll: aplica(lambda x: x*x,ll)
ff(lista)
print lista

# Las funciones también las podemos definir dentro de otras
# funcinoes y usarlas como valor de retorno
# el concepto se llama "high order functions"
def realpath(pre,pos):
    def ff(ss):
        return pre+ss+pos
    return ff
# la función devuelta se trae los valores de pre y pos
# de cuando fue definida
imgp = realpath('/home/jorgeu/img/','.jpg')
pdfp = realpath('/var/lib/pdf/','.pdf')
print imgp('avatar')
print imgp('bebe')
print pdfp('brochure')
print pdfp('report')

# otro ejemplo
def polinomio(factores):
    def evaluar(x):
        valor, exp = 0, len(factores)-1
        for idx in range(len(factores)):
            valor += factores[idx] * x**exp
            exp = exp - 1
        return valor
    return evaluar

# 2 * x^2 + 3 * x + 5
p1 = polinomio([2, 3, 5])
print p1(2)

# ejercicio
# escriba una función que permita saber si una cadena
# es palindroma

# tip: s[::-1] devuelve la cadena s en orden reverso
