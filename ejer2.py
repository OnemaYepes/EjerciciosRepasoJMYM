def area_circulo(radio):
    area = 3.1416*radio**2
    return area

radio = float(input("Ingresa el radio del círculo: "))
area = area_circulo(radio)
print("-"*17,"\nEl círculo de radio", radio,"tiene un área de", area,"unidades cuadradas")