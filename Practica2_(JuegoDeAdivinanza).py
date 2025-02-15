#Mejora el juego de adivinanza que hicimos anteriormente. Ahora, el programa debe:
#1.- Generar un número aleatorio entre 1 y 100.
#2.- Dar pistas al usuario si el número ingresado es mayor o menor que el número secreto.
#3.- Limitar el número de intentos a 5.

import random
import os

intentos = 5

numero_desconocido = random.randint (1, 100)
adivinado = False


while not adivinado:
    if intentos == 0:
        print ("PERDISTE. Te quedaste sin intentos.")
        break

    os.system ('cls')

    print ("ADIVINA EL NÚMERO DEL 1 AL 100")
    numero = int(input("Adivina el número: "))
    if numero == numero_desconocido:
        print ("¡¡¡ADIVINASTE!!!")
        adivinado = True
    elif numero > numero_desconocido:
        print ("ERROR. El número desconocido es MENOR")
        intentos -= 1
        print (f"Te quedan {intentos} intentos.")
        input ("")  
    else:
        print ("ERROR. El número desconocido es MAYOR")
        intentos -= 1
        print (f"Te quedan {intentos} intentos.")
        input ("")
        
     