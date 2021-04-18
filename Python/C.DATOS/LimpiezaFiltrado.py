import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\diego\\Documents\\B45C4R0\\Python\\C.DATOS\\LimpiezaFiltrado.csv")

print(data)

#Verifica que campo esta vacío, y me retorna un True si lo esta, de lo contrario un False
#print(data.isnull())

#Me retorna todas la filas en donde no encuentra ningun campo vacío(Donde todos los campos tienen valores)
#print(data.dropna(axis=0, how='any'))

#Me elimina toda la fila en la cual esten todos los campos vacios
#print(data.dropna(axis=0, how='all'))

#Me retorna las columnas que no contienen ningun campo vacío
#print(data.dropna(axis=1, how='any'))

#Aquellos campos que esten vacíos les cambia el valor a el que se desee, en este caso a 3
#print(data.fillna(value=3))

#Toma la media de una columna(num) y la coloca en los campos NaN de esa misma columna
#print(data.fillna(data.mean()))

#Cambia los valores vacios por el valor que este por debajo de el
#print(data.fillna(method='bfill', limit=1))


#/*************************************************************************\

#Me retorna un booleano(True) si se cumple la condición dada, sino un (False)
#Preguntamos si en la columna cedula hay valores mayores o iguales a 10000000
#print(data['cedula'] >= 10000000)

#Me retorna todas las filas en las cuales la condición dada es verdadadera
#print(data[data['cedula'] >= 10000000])

#Me retorna el valor como tal de la columna cuando se cumple la condición
#print(data['cedula'][data['cedula'] >= 10000000])

#Me retorna las filas en las cuales se cumplen ambas condiciones
#print(data[(data['cedula'] >= 10000000) & (data['primernombre'] == "MARIA")])

#/*************************************************************************\
#Me toma la fila en donde NO cumple la condicion y la pone toda en NaN
#print(data.where(data['cedula']>= 10000000))
#Me toma la fila en donde NO cumple la condicion y la pone toda en el valor que desee,
#ya sea una operacion, o dependiendo de mis valores vecinos con .fillna
#print(data.where(data['cedula']>= 10000000, "No CUMPLE"))

#Me toma la fila en donde SI cumple la condicion y la pone toda en NaN
#print(data.mask(data['cedula']>= 10000000))
#Me toma la fila en donde SI cumple la condicion y la pone toda en el valor que desee.
#ya sea una operacion, o dependiendo de mis valores vecinos con .fillna
#print(data.mask(data['cedula']>= 10000000, "CUMPLE"))
#print(data.mask(data['cedula']>= 10000000, data.fillna(method='backfill', limit=5)))
#print(data.mask(data['cedula']>= 10000000, data.fillna(method='pad', limit=3)))

#La diferencia es que al pasar una lista es como si lo evaluara en toda la DataFrama,
#en cambio con un diccionario evalua los valores en una columna o columnas especificas
#Ambos retornan un booleano
#print(data.isin(["MARIA"]))
#print(data.isin({"primernombre":["MARIA"]}))

#Query es para pregunta algo, y muestra la fila en donde se cumple 
#y Eval es además para hacer operaciones entre columnas, y me arroja la columna con el resultado
#En este espacio añadí la columna num para verificar que sucedia
#print(data.query('cedula>num'))
#print(data.eval('cedula+num'))

