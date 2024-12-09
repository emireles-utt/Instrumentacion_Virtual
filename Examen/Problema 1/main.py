arrayBin = []                   #lista que contiene el valor en binario
arrayHexa = []                  #lista que contiene el valor en hexadecimal


''' Esta funcion recibe un numero decimal y lo convierte a su equivalente en binario.
    El algoritmo convierte a binario usando el metodo de las divisiones sucesivas entre 2.
    La lista debe tener un tamaño que sea multiplo de 4 para facilitar la conversion a 
    hexadecimal.'''


def binario(numero):
    while numero > 0:           #mientras el cociente sea mayor a cero iteremos
        temp = numero % 2       #extraemos el digito binario del residuo usando el modulo
        arrayBin.append(temp)   #agregamos el digito binario en la lista
        numero //= 2            #dividimos el numero usando una division entera para seguir iterando

    tamanio = len(arrayBin)     #obtenemos el numero de elementos de la lista
    while tamanio % 4 != 0: #determinamos si la lista es multiplo de 4
        arrayBin.append(0)      #en caso de que no sea multiplo de 4 llenamos los espacios con ceros
        tamanio = len(arrayBin) #determinamos nuevamente el tamaño de la lista


def hexadecimal(numero):
    while numero > 0:  # mientras el cociente sea mayor a cero iteremos
        temp = numero % 16  # extraemos el digito binario del residuo usando el modulo
        if temp >= 10 and temp <= 15:
            temp = chr(temp + 55)
        arrayHexa.append(temp)  # agregamos el digito binario en la lista
        numero //= 16  # dividimos el numero usando una division entera para seguir iterando


''' Funcion principal '''
if __name__ == "__main__":
    num = int(input("Dame un numero: ")) #pedimos el numero a convertir
    binario(num)                    #llamamos a la funcion binario y le pasamos el numero que deseamos convertir
    arrayBin.reverse()              #invertimos el orden de la lista
    print(num)                      #imprimimos el numero decimal
    print(arrayBin)                 #imprimimos la lista binaria
    hexadecimal(num)                   #llamamos a la funcion hexdecimal para convertir la lista binaria a hexa
    arrayHexa.reverse()             #invertimos el orden de la lista
    print(arrayHexa)                #imprimimos la lista
