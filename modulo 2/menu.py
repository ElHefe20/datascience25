#menu while

opcion = ""
while opcion !="4":
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. salir")
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 - numero2
        print(f"La resta de {numero1} y {numero2} es: {resultado}")
    elif opcion == "3":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 * numero2
        print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor intente de nuevo.")
