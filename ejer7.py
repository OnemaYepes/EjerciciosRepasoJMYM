cant_lista = int(input("Ingrese la cantidad de números de la lista: "))

lista = []

for i in range(cant_lista):
    num = float(input("Ingresa el número: "))
    lista.append(num)

num_grande = max(lista)
num_pequeno = min(lista)

print("-"*17,"\nNúmero más grande es:", num_grande)
print("Número más pequeño es:", num_pequeno)