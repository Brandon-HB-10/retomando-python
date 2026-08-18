def convertir_salarios(salarios):
    resultados = []

    for salario in salarios:
        try:
            salario_convertido = int(salario)
            resultados.append(salario_convertido)
        except (ValueError, TypeError):
            continue 
    
    return resultados 

salarios = ["20000", None, "no disponible", " 15000 ", 18000]


print(convertir_salarios(salarios))

assert convertir_salarios(
    ["20000", None, "no disponible", " 15000 ", 18000]
) == [20000, 15000, 18000]

assert convertir_salarios([]) == []

assert convertir_salarios(
    [None, "", "desconocido"]
) == []

print("Todas las pruebas pasaron")