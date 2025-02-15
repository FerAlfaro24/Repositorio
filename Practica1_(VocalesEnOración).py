texto = input ("Ingrese el texto: ")
vocales = "aeiouAEIOU"
contador = 0
                        
for letra in texto:
    if letra in vocales:
        contador += 1

print ("El número de vocales es: ", contador)