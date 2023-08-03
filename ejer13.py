num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1+num2
resta = num1-num2
producto = num1*num2

if num2 == 0:
    division = "Math ERROR"
else:
    division = num1/num2

print("---------\nLa suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", producto)
print("La división es:", division)