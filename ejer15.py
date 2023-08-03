def palindromo(texto):
    texto_junto = texto.replace(" ", "")
    texto_minusculo = texto_junto.lower()
    texto_invertido = texto_minusculo[::-1]

    if texto_minusculo == texto_invertido:
        return True
    else:
        return False
    
cadena_texto = input("Ingrese una cadena de texto para verificar si es palíndromo:\n")
if palindromo(cadena_texto):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo :c")