"""

Integrantes:
Diego Alonso Galeano Herrera - 20172020074
Oscar David Rubiano Diaz - 20201020083
Diego Alejandro Bautista Castañeda - 20192020139

"""

import pandas as pd
 
data = pd.read_csv('C:\\Users\\diego\\Documents\\B45C4R0\\Python\\C.DATOS\\phone_data.csv', index_col='index')
print(data)

#1) ¿Cuál fue la llamada de mayor duración?
print(data[data['duration']==data['duration'][data['item'] == 'call'].max()])

#2) ¿Cuál fue el evento de datos de mayor duración?
print(data[data['duration']==data['duration'][data['item'] == 'data'].max()])

#3) ¿Cuánto fue el total de segundos entre sms y eventos de datos?
print(data['duration'][data['item'] == 'sms'].sum() + data['duration'][data['item'] == 'data'].sum())

#4) ¿Cuantas entradas de datos hay por cada uno de las redes?
print(data['network'][data['item'] == 'data'].value_counts())

#5) ¿Cuantas entradas de llamada hay por cada una de las redes?
print(data['network'][data['item'] == 'call'].value_counts())

#6) Obtener el promedio de llamadas por cada una de las redes
print(data.groupby(data['network'][data['item'] == 'call'])['duration'].mean())

#7) Obtener el promedio de eventos de datos por cada una de las redes
print(data.groupby(data['network'][data['item'] == 'data'])['duration'].mean())

#8) Obtener el número de entradas tipo llamada por cada una de las redes
print(data.groupby(data['network'][data['item'] == 'call']).count())

#9) Obtener el número de entradas tipo sms por cada una de las redes
print(data.groupby(data['network'][data['item'] == 'sms']).count())

#10) Por cada uno de los meses, ¿cuántas veces se usaron cada una de las redes (para cualquier evento)?
print(data.groupby(['month', 'network'])['item'].count())

#11) Por cada uno de los meses, ¿cuántas veces se usaron cada una de las redes discriminando el tipo de evento?
print(data.groupby(['month', 'network','item']).count())


