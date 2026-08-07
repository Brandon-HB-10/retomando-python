def es_palindromo(palabra):
    if palabra == palabra [::-1]:
        return True 
    else:
        return False 

print(es_palindromo("reconocer"))
print(es_palindromo("computadora"))