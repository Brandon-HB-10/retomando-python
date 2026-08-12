vacantes = [
    {"puesto": "Backend Python", "remoto": True, "salario": 20000},
    {"puesto": "Soporte TI", "remoto": False, "salario": 14000},
    {"puesto": "Data Intern", "remoto": True, "salario": 16000}
]

def filtrar_vacantes_remotas(vacantes):
    resultados = []
    for vacante in vacantes:
        if vacante["remoto"]:
            resultados.append(vacante["puesto"])
    return resultados 

print(filtrar_vacantes_remotas(vacantes))


assert filtrar_vacantes_remotas(vacantes) == [
    "Backend Python",
    "Data Intern"
]

assert filtrar_vacantes_remotas([]) == []

assert filtrar_vacantes_remotas([
    {"puesto": "Soporte TI", "remoto": False}
]) == []