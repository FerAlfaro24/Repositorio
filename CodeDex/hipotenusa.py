#Calcular la hipotenusa de 2 catetos

catetoa = int(input("Ingresa el valor del cateto A: "))
catetob = int(input("Ingresa el valor del cateto B: "))

hipotenusa = ((catetoa ** 2)+(catetob ** 2))**0.5

print ("La hipotenusa tiene un valor de: ", hipotenusa)