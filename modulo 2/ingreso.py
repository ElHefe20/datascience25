usuario =input("ingrese su usuario: ")
contraseña = input("ingrese su contraseña: ")
if usuario == "admin" and contraseña == "1234":
    print("acceso concedido")
else :
    print("acceso denegado")

#programa que valide capital de chile
capital= "santiago"
ingresecapital= input("ingrese capital de chile: ")
if ingresecapital == "santiago":
    print("es correcto")
else :
    print(" es incorrecto")

capital = input("cual es la capital de chile: ")
if capital.upper()== "SANTIAGO":
    print("bien hecho, la capital de Chile es Santiago")
else:
    print("lo siento, la capital de Chile es Santiago")

