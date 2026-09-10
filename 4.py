import pandas as pd
df= pd.read_csv('ModalidadVirtual.csv')

print(df.head())
print(df.head(10))

print(df['carrera'][1])
print(df['edad'] > 23)

filtrar=df['edad'] > 23
df_filtrar= df[filtrar]

print(df_filtrar)
print(df.tail(10))

