def invertir(lista):
    lista_inversa = []
    for i in range(len(lista) -1, -1, -1):
        lista_inversa.append(lista[i])
    return lista_inversa



cant_lista = int(input("Ingrese la cantidad de números de la lista: "))
lista = []

for i in range(cant_lista):
    num = float(input("Ingresa el número: "))
    lista.append(num)

lista_invertida = invertir(lista)
print("-"*17,"\nLa lista invertida queda así:", lista_invertida)