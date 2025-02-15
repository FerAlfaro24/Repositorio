import random

numero_secreto = random.randint (1, 10)
adivinado = False
contador = 1

while not adivinado:
    numero = int(input("Adivina un número del 1 al 10: "))
    if numero == numero_secreto:
        print ("Correcto. Adivinaste")
        adivinado = True
        contador += 1

    else:
        print ("Te equivocaste jijiji pendejo")

print(f"Te tomó {contador} intentos")
