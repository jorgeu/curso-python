# -*- coding: UTF-8 -*-

import psycopg2      # http://initd.org/psycopg/

# conexión con tipo cursor por defecto
constr="host='localhost' dbname='python' user='postgres' password='123'"
conn = psycopg2.connect(constr)
cursor = conn.cursor()
cursor.execute("select * from persona")
personas = cursor.fetchall()
for p in personas:
    print "id: %d nombre: %s" % (p[0],p[1])
    
# ahora vemos otro tipo de cursor que permite usar 
# los nombres de las columnas
import psycopg2.extras
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("select * from persona")
personas = cursor.fetchall()
for p in personas:
    print "id: %d nombre: %s" % (p['id'],p['nombre'])
    
# las actualizaciones a la base de datos funcionan de manera similar
cursor.execute("insert into persona(nombre) values(?)",('Manuel',))

cursor.close()
conn.close()


