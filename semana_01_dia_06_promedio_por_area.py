vacantes = {
    "area": ["Backend", "Datos", "Backend", "Soporte", "Datos"],
    "salario": [20000, 18000, 24000, 14000, 22000]
}

import pandas as pd 

df = pd.DataFrame(vacantes)
promedios = df.groupby("area").agg(
    promedio=("salario", "mean"),
    cantidad=("salario", "count")
).reset_index()

print(promedios)