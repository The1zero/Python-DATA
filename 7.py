import pandas as pd

#Se agrega set_index para que la columna Nombre sea el índice del dataframe
DF1 = pd.DataFrame({'Nombre':['Jose','Max'],
'Carreras':['Economia','Arquitectura'],
'Edad':[23,26]}).set_index('Nombre')

DF2 = pd.DataFrame({'Nombre':['Aurora','Maria'],
'Carreras':['Medicina','Informatica'],
'Edad':[22,28]}).set_index('Nombre')

#Combinamos dataframes
DF=pd.concat([DF1,DF2])

print(DF1)
print(DF2)
print(DF)

