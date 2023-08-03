import random

can_num = int(input("Ingrese la cantidad de números aleatorios: "))

num_aleatorios = [0]*can_num
for i in range(can_num):
    num_aleatorios[i]= int(random.random()*1000)

print("-"*17,"\nLos números son:")
print(num_aleatorios)