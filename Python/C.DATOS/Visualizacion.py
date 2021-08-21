# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Python\C.Datos\ign.csv", index_col='id')


#data = data["release_year"].unique()

d1 = data['frase_score'].dropna().value_counts().sort_index(ascending=True)
#d2 = data['Fecha de muerte'].dropna().apply(dateutil.parser.parse, yearfirst=True).value_counts().sort_index(ascending=True)
#d3 = data['Fecha recuperado'].dropna().apply(dateutil.parser.parse, yearfirst=True).value_counts().sort_index(ascending=True)

print(d1.plot())
# %%
