import pandas as pd

DF1 = pd.DataFrame({'Autos':['Nissan','Ford','Audi'],
'Color':['Blanco','Azul','Rojo']}).set_index('Autos')

DF2 = pd.DataFrame({'Autos':['Nissan','Ford','Audi'],
'Modelo':['2018','2020','2022']}).set_index('Autos')

#Combinacion por columnas. Se pone axis=1 para indicar que se combinan por columnas. Si se quisiera combinar por filas, se pondria axis=0
DF=pd.concat([DF1,DF2],axis=1)
print(DF)