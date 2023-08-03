def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact

num = int(input("Digite un #Entero para conocer su factorial: "))
resultado = factorial(num)
print("-"*17,"\nEl factorial de", num,"! es: ",resultado)