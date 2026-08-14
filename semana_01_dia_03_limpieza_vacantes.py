vacantes = [
    {"puesto": " Backend Python ", "salario": "20000"},
    {"puesto": "DATA INTERN", "salario": "16000"},
    {"puesto": "Soporte TI", "salario": None}
]

def limpiar_vacantes(vacantes):
    resultados = []
    for vacante in vacantes:
        if vacante["salario"] is not None:
            salario_limpio = int(vacante["salario"])
            puesto_limpio = vacante["puesto"].strip().lower()
            vacante_limpia = {
                "puesto": puesto_limpio,
                "salario": salario_limpio
                }
            resultados.append(vacante_limpia)

    return resultados

print(limpiar_vacantes(vacantes))

assert limpiar_vacantes(vacantes) == [
    {"puesto": "backend python", "salario": 20000},
    {"puesto": "data intern", "salario": 16000}
]

assert limpiar_vacantes([]) == []
