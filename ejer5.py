def fah_cel(grados_f):
    grados_c = (grados_f-32)*5/9
    return grados_c

grados_f = float(input("Ingrese los grados en Fahrenheit: "))
grados_c = fah_cel(grados_f)

print("-"*17,"\n",grados_f, "°F equivalen a", grados_c,"°C")