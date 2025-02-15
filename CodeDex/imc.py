#Crear un bmi.p programa que calcula su propio IMC.

peso = int(input("Ingresa su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

imc = (peso)/(altura**2)

print ("Su índice de masa corporal(IMC) es: ", imc)