contador = 0

while True:
    numero = int(input("Ingresa el número 0 para terminar: "))
    if numero == 0:
        print ("Saliendo del programa")
        break
    else:
        print ("El número que ingresaste fue: ", numero)
        contador += numero

print ("La suma de los números que pusiste es: ", contador)