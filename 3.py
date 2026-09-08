import pandas as pd
import numpy as np
data = {'nombre':['Maria','Jose','David','Ivan'], 
        'Carrera':['Auditoria','Informatica','Derecho','Idiomas'],
        'Correo':['maria@universidad.edu','jose@universidad.edu','david@universidad.edu','ivan@universidad.edu']}

estudiantes = pd.DataFrame(data)
print(estudiantes)

df=pd.DataFrame([['Maria',27],['David',30],['Ana',18],['Jose',17]],
                columns=['Nombre','Edad'])

print(df)

#Creacion de un dataframe con valores aleaotrios. Con un array numpy
df2 = pd.DataFrame(np.random.randn(4,3),columns=['a','b','c'])
print(df2)