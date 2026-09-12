import pandas as pd 

df = pd.read_csv('Estudiantes.csv')
print(df)

convertir = pd.read_excel('Estudiantes.xlsx')
convertir.to_csv('EstudiantesConvertido.csv', index=None, header=True)