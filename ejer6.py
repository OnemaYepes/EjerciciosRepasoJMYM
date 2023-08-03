cant_lista = int(input("Ingrese la cantidad de números de la lista: "))

lista = []

for i in range(cant_lista):
    num = float(input("Ingresa el número: "))
    lista.append(num)

suma = sum(lista)

print("-"*17,"\nEl resultado de sumar", lista,"es: ",suma)
