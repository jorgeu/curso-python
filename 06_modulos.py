# -*- coding: UTF-8 -*-

# esto va a buscar sys.py en el PYTHONPATH
import sys 
print sys.version

# podemos traernos solamente una miembro específico
from sys import version
print version

# o simplemente todo
from math import *
print sqrt(9)

# función dir() nos permite ver qué hay en un módulo u objeto
dir(sys)
dir(sys.path) # este es una lista

