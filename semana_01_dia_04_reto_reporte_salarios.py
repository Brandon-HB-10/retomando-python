def procesar_salarios(salarios):
    validos = []
    rechazados = 0
    for salario in salarios:
        try:
            
            salario_convertido = int(salario)
            validos.append(salario_convertido)
        except (ValueError, TypeError):
            rechazados += 1 
            continue
    return { "validos": validos,
             "rechazados": rechazados 
             }

salarios = ["20000", None, "no disponible", " 15000 ", 18000]

print(procesar_salarios(salarios))

assert procesar_salarios(
    ["20000", None, "no disponible", " 15000 ", 18000]
) == {
    "validos": [20000, 15000, 18000],
    "rechazados": 2
}

assert procesar_salarios([]) == {
    "validos": [],
    "rechazados": 0
}

assert procesar_salarios([None, "", "error"]) == {
    "validos": [],
    "rechazados": 3
}

print("Todas las pruebas pasaron")