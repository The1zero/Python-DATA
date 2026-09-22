import pandas as pd

DF1 = pd.DataFrame({'Autos':['Nissan','Ford','Audi'],
'Color':['Blanco','Azul','Rojo']})

DF2 = pd.DataFrame({'Autos':['Nissan','Ford','Audi'],
'Modelo':['2018','2020','2022']})

#cambiar nissan por toyota para ver el efecto de outer join
DF2 = pd.DataFrame({'Autos':['TOYOTA','Ford','Audi'],
'Modelo':['2018','2020','2022']})

#Mezclar informacion en comun. Inerr por defecto, outer por filas
DF=pd.merge(DF1,DF2, on='Autos', how='outer')