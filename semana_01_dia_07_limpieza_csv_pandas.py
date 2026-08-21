import pandas as pd

#Extract: extraer datos del CSV
df = pd.read_csv("vacantes.csv")

#Transform: convertir y limpiar
df["salario"] = pd.to_numeric(
    df["salario"],
    errors="coerce"
)

cantidad_sin_salario = df["salario"].isna().sum()
promedio_salario = df["salario"].mean()

df_limpio = df.dropna(subset=["salario"]).copy()

print(df)
print(df.dtypes)

print("Salarios no disponibles:", cantidad_sin_salario)
print("Promedio de salarios conocidos:", promedio_salario)

print("\nDataFrame limpio:")
print(df_limpio)

#Load: guardar el resultado procesado.
df_limpio.to_csv("vacantes_limpias.csv", index=False)


df_verificacion = pd.read_csv("vacantes_limpias.csv")

assert len(df_verificacion) == 2
assert df_verificacion["salario"].isna().sum() == 0

print("Verificación completada correctamente")