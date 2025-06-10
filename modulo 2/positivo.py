#programa apra saber si un numero es positivo o negativo
numero = int(input("ingrese un numero: "))
if numero>=0 :
    print("el numero es positivo")
else:
    print("el numero es negativo")
usuario =input("ingrese su usuario: ")
contraseña = input("ingrese su contraseña: ")
if usuario == "admin" and contraseña == "1234":
    print("acceso concedido")
else :
    print("acceso denegado")


#numero par o impar
paridad = "par" if numero % 2 ==0 else "impar"
print(f"Este es un numero {paridad} el numero es {numero}")
print(paridad)