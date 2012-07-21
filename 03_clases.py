# -*- coding: UTF-8 -*-

# Las clases se definen con la palabra class
# aplican las mismas reglas de los bloques 

class Persona: pass    # pass permite dejar vacío

# tienen dos tipos de 'miembros': datos y métodos
# los datos se pueden ver como varibles de instancia

class Persona: 
    nombre = ''  # inicializamos nombre con cadena vacía

# en python no hay tal cosa como miembros privados
# hay una convención no forzada que si el miembro
# comienza con al menos un _ en su nombre entonces 
# no se le debería llamar fuerad de la definición 
# de la clase. Por otro lado si tiene al menos dos _
# entonces internamente se le agrega _classname__nombre
# la idea es diferenciarlo en subclases

class Persona:
    __nombre = 'fulano'

jorge = Persona()
jorge.__nombre='jorge'

# los métodos lucen como funcinoes normales pero siempre
# van a recibir como primer parámetro la instancia actual
# (lo que en otros lenguajes es this). La convención es
# llamarle self

class Persona:
    __nombre='fulano'
    def getNombre(self):
        return self.__nombre

jorge = Persona()
print jorge.getNombre()

# para definir un constructor se usa el nombre de método especial
# __init__

class Persona:
    def __init__(self, n):
        self.__nombre=n
        
    def __str__(self):
        # transformación a string por defecto
        return "<"+self.__nombre+">"

jorge = Persona('Jorge')
print jorge

# la herencia en python es simple. Al definir la clase
# se indica la clase base entre ()
class Estudiante(Persona):
    def __init__(self, n, carrera):
        Persona.__init__(self,n)
        self.__carrera=carrera
   
    def __str__(self):
        return "<"+self._Persona__nombre+","+self.__carrera+">"

e = Estudiante('Raul','Computación')
print e

# Note que para hacer referencia a __nombre en la clase base
# tenemos que usar el prefijo _Persona
# de esta manera podemos definir __nombre en Estudiante sin
# dañar la clase base. Esa característica se llama 'name mangling'
# eso sólo es necesario en variables de instancia con doble _



# Los iteradores son objetos que tienen un método next()
# son útiles para abstraer el recorrido de datos secuenciales
# de un objeto
class Materia:
    def __init__(self,nombre):
        self.nombre=nombre
    def __str__(self):
        return self.nombre

class Programa:
    def __init__(self,materias=[]):
        self.materias=materias
        
    def addMateria(self,m):
        self.materias.append(m)
    
    def __iter__(self):
        self.iter_idx=0
        return self
        
    def next(self):
        if(self.iter_idx==len(self.materias)):
            raise StopIteration
        v = self.materias[self.iter_idx]
        self.iter_idx = self.iter_idx + 1
        return v

diseno = Programa([Materia('dibujo'),Materia('publicidad')])
print 'Materias:'
for m in diseno:
    print m


# Otra forma te iterar es con los generadores
# es como si tuvieramos una función que retorna
# varias veces y sigue donde estaba
def pares(nums):
    for n in nums:
        if (n % 2)==0:
            yield n

xx=range(1,20)
for x in pares(xx):
    print x

# otro tipo de generador es el basado en expresión
list(x*x for x in range(20))


