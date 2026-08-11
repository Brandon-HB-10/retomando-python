def contar_vocales(texto):
    vocales = 0
    for letra in texto:
        if letra in "aeiou":
           vocales += 1
    return vocales
    
print(contar_vocales("Python"))