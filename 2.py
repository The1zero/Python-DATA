import pandas as pd

colores = pd.Series(['rojo','azul','verde','amarrillo','morado'])

print(colores)

#diccionario siempre en llaves
materias = pd.Series({'Matematicas':60,'Fisica':70,'Quimica':78})

print(materias)

#Propiedades de serie: 
# .size(numero de elementos)
# .index(una lista con los nombres de las filas del Dataframe)
# .dtype(tipo de dato de los elementos de la serie)

numero=pd.Series([1,2,3,4,5,6,7,8,9,10])
numero.size
numero.index
numero.dtype

colores[1:2]
colores[2:4]
materias["Fisica"]
materias[["Fisica","Quimica"]]