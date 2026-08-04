x = int(input("Introduce un numero entero: "))
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(es_par(x))