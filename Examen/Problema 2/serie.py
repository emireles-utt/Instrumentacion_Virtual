import math
''' Funcion para calcular el factorial de un numero dado '''
def factorial(num):
    acc = 1                     #acumulador para almacenar la multiplicacion del factorial

    for x in range(num):        #calculamos el factorial
        acc *= x + 1

    return acc                  #se retorna el acumulador que

''' Funcion que calcula el coseno y retorna el valor en radianes '''
def serieCos(num):
    cosTemp = 0                 #acumulador que contendra el valor del coseno
    for n in range(501):        #calculamos 500 sumas y restas de la serie
        cosTemp += (((-1) ** n) / factorial(2 * n)) * (num ** (2 * n))  #calculamos el coseno

    return cosTemp              #retornamos el valor del coseno

''' Programa principal '''
if __name__ == "__main__":
    numero = eval(input("Cos de: "))    #se pide el angulo en radianes
    valorCos = serieCos(numero)         #pasamos el valor a la funcion para calcular el coseno
    print(valorCos)                     #mostramos el valor del coseno en pantalla
