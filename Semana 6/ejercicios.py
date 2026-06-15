

#2

## Código de la solución
import pandas as pd

df = pd.DataFrame({
    "P1":[3600],
    "P2":[7200],
    "P3":[5000]
})

df.loc[1] = df.loc[0].apply( lambda x: x / 3600)

print(df)



##4 Código de la solución
import pandas as pd
# Datos iniciales
datos = {'Estudiante': ['Grettel', 'Paula', 'Walter', 'Vinicio'], 'Nota': [85, 60, 58, 92]}

dfestudiantes = pd.DataFrame(datos)

print(dfestudiantes)

print(dfestudiantes['Nota'])