frutas = ('manzana', 'plátano', 'naranja', 'pera', 'uva', 'kiwi', 'mango', 'pera')

# Variable para almacenar la lista convertida
lista_frutas = None

while True:  # Cambiamos a un bucle infinito con control explícito de salida
    print("\n1. Ver todas las frutas")
    print("2. Contar cuántas veces aparece una fruta específica")
    print("3. Convertir la tupla a lista y agregar una fruta")
    print("4. Mostrar el inventario actualizado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    # Opción 1: Ver todas las frutas
    if opcion == "1":
        print("\nLista de frutas:")
        for i, fruta in enumerate(frutas, 1):
            print(f"{i}. {fruta}")
    
    # Opción 2: Contar una fruta específica
    elif opcion == "2":
        fruta_buscada = input("\nIngrese el nombre de la fruta que desea contar: ").strip().lower()
        
        # Convertimos a minúsculas para comparar
        fruta_buscada = fruta_buscada.lower()
        
        # Contar la fruta en la tupla original
        contador = frutas.count(fruta_buscada)
        
        
        # Mostrar el resultado
        if contador > 0:
            veces = "vez" if contador == 1 else "veces"
            print(f"\nLa fruta '{fruta_buscada.title()}' aparece {contador} {veces} en el menú.")
        else:
            print(f"\nLa fruta '{fruta_buscada.title()}' no aparece en el menú.")
    
    # Opción 3: Convertir a lista y agregar fruta
    elif opcion == "3":
        # Convertir la tupla a lista si aún no se ha hecho
        if lista_frutas is None:
            lista_frutas = list(frutas)
        
        # Pedir al usuario una nueva fruta
        fruta_nueva = input("\nIngrese el nombre de la nueva fruta (deje vacío para cancelar): ").strip().lower()
        
        # Si se ingresó una fruta, agregarla a la lista
        if fruta_nueva:
            # Verificar si ya existe en la lista
            if fruta_nueva in lista_frutas:
                print(f"La fruta '{fruta_nueva.title()}' ya se encuentra en la lista.")
            else:
                lista_frutas.append(fruta_nueva)
                print(f"Fruta '{fruta_nueva.title()}' agregada correctamente.")
    
    # Opción 4: Mostrar el inventario actualizado
    elif opcion == "4":
        if lista_frutas is not None:
            print("\nInventario actualizado:")
            for i, fruta in enumerate(lista_frutas, 1):
                print(f"{i}. {fruta}")
        else:
            print("\nPrimero debes convertir la tupla a lista (opción 3).")
    
    # Opción 5: Salir
    elif opcion == "5":
        print("\nSaliendo del programa...")
        break
    
    # Opción inválida
    else:
        print("\nOpción no válida. Por favor intente de nuevo.")