#Crear un moneda.py programa que le pide al usuario la cantidad que tiene 
# en pesos, soles y reales y calcula el total en USD.

pesos = float(input("Ingresa los pesos colombianos: "))
soles = float(input("Ingresa los soles peruanos: "))
reales = float(input("Ingresa los reales brasileños: "))

dolares = (pesos * 0.00024) + (soles * 0.27) + (reales * 0.17)

print(f"Tienes {dolares:.2f} dólares")
