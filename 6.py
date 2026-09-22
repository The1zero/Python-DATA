import pandas as pd

df=pd.read_csv('EstudiantesConvertido.csv')
print(df)

print(df.iloc[1,3])

print(df.iloc[2,:3])

print(df.loc[1,'Carrera'])

print(df.loc[:3,('Carrera','Nombre')])

print(df.iloc[1, :3])

df2 = df.copy()
df['TURNO'] = pd.Series(['tarde','noche','tarde','noche','noche','tarde'])

print(df)

Semestre = df.pop('Semestre')

print(df)

df=df.append(pd.Series(['Carlos',27,'M','Sociologia','tarde'],
index=['Nombre','Edad','Genero','Carrera','TURNO']),ignore_index=True)

print(df)

print(df.drop([1,2]))

print(df[(df['Genero']=='F') & (df['Edad'] >= 22)])

print(df.sort_values('Carrera'))
print(df.sort_values('Edad'))
print(df.dropna())