vacantes = [
    {"puesto": "Backend Python", "remoto": True, "salario": 20000},
    {"puesto": "Soporte TI", "remoto": False, "salario": 14000},
    {"puesto": "Data Intern", "remoto": True, "salario": 16000}
]

def calcular_promedio_salario_remoto(vacantes):
    suma_salarios = 0 
    cantidad_remotas = 0 
    for vacante in vacantes:
        if vacante["remoto"]:
            suma_salarios += vacante["salario"]
            cantidad_remotas += 1 
    if cantidad_remotas == 0:
        return 0

    return suma_salarios / cantidad_remotas

print(calcular_promedio_salario_remoto(vacantes))



assert calcular_promedio_salario_remoto(vacantes) == 18000
assert calcular_promedio_salario_remoto([]) == 0
assert calcular_promedio_salario_remoto([
    {"puesto": "Soporte", "remoto": False, "salario": 14000}
]) == 0