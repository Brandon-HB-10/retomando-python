def contar_tecnologias(tecnologias):
    conteo = {}
    for tecnologia in tecnologias:
        tecnologia = tecnologia.strip().lower()

        if tecnologia == "":
            continue 
        if tecnologia in conteo :
            conteo[tecnologia] += 1 
        else:
            conteo[tecnologia] = 1 
    return conteo

print(contar_tecnologias(
    ["Python", "SQL", "python", "Git", "SQL", " Python "]
))

assert contar_tecnologias(["Python", "python"]) == {"python": 2}
assert contar_tecnologias([]) == {}
assert contar_tecnologias([" SQL "]) == {"sql": 1}
assert contar_tecnologias(
    ["Python", " ", "", "SQL"]
) == {"python": 1, "sql": 1}