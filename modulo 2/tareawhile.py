# Escribe un programa en Python que recorra cada letra
# de una palabra utilizando un ciclo while.
# El programa debe imprimir la posición de cada letra
# y la letra correspondiente.
# Por ejemplo, si la palabra es "gato", el programa debe mostrar:
 
# Letra en posición 0: g  
# Letra en posición 1: a  
# Letra en posición 2: t  
# Letra en posición 3: o

frase = input("ingrese una frase: ")
inicio = 0

while inicio != len(frase):
    print(f"La letra {frase[inicio]} está en la posición {inicio} de la frase: {frase}")
    inicio +=1

#otro programa
palabra = input("Introduce uuna palabra: ")
indice = 0
print(len(palabra))
while indice< len(palabra):
    print(f"Letra en posicion {indice}: {palabra[indice]}")
    indice += 1    

