#Crea un programa que verifique si un estudiante aprobó o reprobó un examen. 
# La calificación mínima para aprobar es 60.
#Requisitos:
#Define una variable grade con un valor entre 0 y 100.
#Usa una estructura if/else para imprimir:
#"You passed!" si la calificación es mayor o igual a 60.
#"You failed." si la calificación es menor a 60.

#SE PUEDE MEJORAR MUCHO


while True:
    try:
        grade = int(input("Agrega la calificación del alumno (0-100): "))
        if grade < 0 or grade > 100:
            print ("Calificación inválida. Ingrese otra.")
        else:
            if grade < 60:
                print ("Reprobaste")
            elif grade < 70:
                print ("Pasaste")
            elif grade < 90:
                print ("Muy bien")
            else:
                print ("EXCELENTE")  
            break
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
  





