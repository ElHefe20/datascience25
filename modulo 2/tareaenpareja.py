# Desarrolla un programa en Python que permita al usuario ingresar  4 números
#realizar operaciones aritméticas con ellos.
# Usa un menú interactivo con las siguientes opciones:
 
 
# Calcular y mostrar la suma total de los números ingresados.
 
# Calcular y mostrar el promedio de los números.
 
# Mostrar el número mayor y menor de la lista.
 
# Salir del programa.
 
# El menú debe repetirse usando un ciclo while
# hasta que el usuario elija salir.
# Asegúrate de validar las entradas numéricas

opcion = ""
while opcion !="4":
    print("1. suma total numeros ingresados")
    print("2. Promedio de numeros")
    print("3. Mostrar numero mayor y menor de la lista")
    print("4. salir del programa")
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))
        resultado = numero1 + numero2 + numero3 +numero4
        print(f"La suma de {numero1},{numero2},{numero3},{numero4} es: {resultado}")
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))
        resultado = (numero1 + numero2 +numero3 +numero4)/4
        print(f"El promedio de {numero1},{numero2},{numero3},{numero4} es: {resultado}")
    elif opcion == "3":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
        numero4 = float(input("Ingrese el cuarto número: "))    
        print(
        print(

       
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor intente de nuevo.")