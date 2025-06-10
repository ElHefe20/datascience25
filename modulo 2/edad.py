#Crea un programa en Python que pida al usuario su edad y
# luego muestre una clasificación según el rango de edad ingresado.
# Las categorías son las siguientes:
# Menos de 0: "Edad inválida"
# De 0 a 12 años: "Niño"
# De 13 a 17 años: "Adolescente"
# De 18 a 59 años: "Adulto"
# 60 años o más: "Adulto mayor"
#que no acepte edades negativas ni mayores a 120

edad = int(input("ingrese su edad en años: "))
if edad > 120 or edad <0:
    print("edad invalida")
else:
    if edad >= 0 and edad <=12:
        print("Niño")
    elif edad >= 13 and edad <=17:
        print("Adolecente")
    elif edad >= 18 and edad <=59:
        print("Adulto")
    elif edad >= 60:
        print("Adulto Mayor")
