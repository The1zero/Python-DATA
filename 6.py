import pandas as pd

df=pd.read_csv('EstudiantesConvertido.csv')
print(df)

print(df.iloc[1,3])

print(df.iloc[2,:3])