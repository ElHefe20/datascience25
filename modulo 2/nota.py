#asignar una letra segun la calificación
calificacion = int(input("ingrese su calificacion: "))
if calificacion > 100 or calificacion <0:
    print("calificacion invalida")
else:
    if calificacion >= 90:
        print("A")
    elif calificacion >= 80:
        print("B")
    elif calificacion >= 70:
        print("C")
    elif calificacion >= 60:
        print("D")
    else:
        print ("F")
