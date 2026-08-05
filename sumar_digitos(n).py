def sumar_digitos(n):
    suma = 0
    for digito in str(n):
        suma += int(digito)

    return suma 
print (sumar_digitos (1234))
print (sumar_digitos (5678))