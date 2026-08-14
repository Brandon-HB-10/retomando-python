def limpiar_vacantes(vacantes):
    resultados = []
    for vacante in vacantes:
        if vacante["salario"] is not None and vacante["salario"].isdigit():
            salario_limpio = int(vacante["salario"])
            puesto_limpio = vacante["puesto"].strip().lower()
            vacante_limpia = {
                "puesto": puesto_limpio,
                "salario": salario_limpio
                }
            resultados.append(vacante_limpia)

    return resultados

vacantes = [
    {"puesto": " Backend Python ", "salario": "20000"},
    {"puesto": "Data Intern", "salario": None},
    {"puesto": "Frontend Junior", "salario": "no disponible"},
    {"puesto": "Soporte TI", "salario": ""},
    {"puesto": "Python Intern", "salario": "15000"}
]

assert limpiar_vacantes(vacantes) == [
    {"puesto": "backend python", "salario": 20000},
    {"puesto": "python intern", "salario": 15000}
]


print(limpiar_vacantes(vacantes))
# Lista vacía
assert limpiar_vacantes([]) == []

# Todos los salarios son inválidos
assert limpiar_vacantes([
    {"puesto": "Soporte", "salario": None},
    {"puesto": "Frontend", "salario": ""},
    {"puesto": "Backend", "salario": "desconocido"}
]) == []

print("Todas las pruebas pasaron correctamente")
