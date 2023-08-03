def media(lista):
    suma = sum(lista)
    prom = suma/len(lista)
    return prom


cant_lista = int(input("Ingrese la cantidad de números de la lista: "))

lista = []

for i in range(cant_lista):
    num = float(input("Ingresa el número: "))
    lista.append(num)

media_arit = media(lista)
print("-------\nLa media aritmética de los elementos de la lista es:", media_arit)