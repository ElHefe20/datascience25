# #  Reto 2: Inventario de Frutas con tupla base
# #  Tienes una tupla con nombres de frutas. Crea un programa con menú que permita:
#  - Ver todas las frutas- 
#  - Contar cuántas veces aparece una fruta específica
#  - Convertir la tupla a lista y agregar una fruta
# #  - Mostrar el inventario actualizado
# - Salir
# #  Utiliza while, tuplas, listas y condicionales.

frutas = ('manzana', 'plátano', 'naranja', 'pera', 'uva', 'kiwi', 'mango','pera')
opcion = ""
while opcion !="4":
    print("1. Ver todas las frutas")
    print("2. Contar cuantas veces aparece una fruta especifica")
    print("3. Convertir la tupla a lista y agregar una fruta")
    print("4. Mostrar el inventario actualizado")
    print("5. Salir")
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        print(frutas)

    elif opcion == "2":
        fruta_buscada = input("Ingrese el nombre de la fruta que desea contar: ").lower()    
        contador = frutas.count(fruta_buscada)
        if contador > 0:
            print(f"La fruta '{fruta_buscada.title()}' aparece {contador} {'veces' if contador > 1 else 'vez'} en el menú.")
        else:
            print(f"La fruta '{fruta_buscada.title()}' no aparece en el menú.")

# Opción 3: Convertir a lista y agregar fruta
    elif opcion == "3":
        lista_frutas = list(frutas)
        # Pedir al usuario una nueva fruta
        fruta_nueva = input(f"Ingrese el nombre de la fruta: ")
        lista_frutas.append(fruta_nueva.lower())

    elif opcion == "4":
        print(lista_frutas)

    elif opcion == "5":
        print("\nSaliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
