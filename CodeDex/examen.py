#Crea un programa que verifique si un estudiante aprobó o reprobó un examen. 
# La calificación mínima para aprobar es 60.
#Requisitos:
#Define una variable grade con un valor entre 0 y 100.
#Usa una estructura if/else para imprimir:
#"You passed!" si la calificación es mayor o igual a 60.
#"You failed." si la calificación es menor a 60.

#SE PUEDE MEJORAR MUCHO

grade = int(input("Agrega la calificación del alumno (0-100): "))

while True:
    if grade < 0 or grade > 100:
        while grade < 0 or grade > 100:
            print ("Calificación inválida. Ingrese otra.")
            grade = int(input("Agrega la calificación del alumno (0-100): "))
    else:
        if grade >= 60:
            print ("Pasaste")
            break
        else:
            print ("Reprobaste")
            break
        
  





