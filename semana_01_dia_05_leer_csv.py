import csv

vacantes_limpias = []

with open(
    "vacantes.csv",
    mode="r",
    encoding="utf-8",
    newline=""
) as archivo:
    
    lector = csv.DictReader(archivo)

    for vacante in lector:
        try:
            salario_convertido = int(vacante["salario"])
            remoto_convertido = (vacante["remoto"]) ==  "True"
            vacante_limpia = {
                "puesto": vacante["puesto"].strip(),
                "empresa": vacante["empresa"].strip(),
                "salario": salario_convertido,
                "remoto": remoto_convertido
            }
            vacantes_limpias.append(vacante_limpia)
        except ValueError:
            continue

print(vacantes_limpias)