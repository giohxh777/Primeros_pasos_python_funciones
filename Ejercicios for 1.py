# ************* zona de funciones *************
#**************ejercicio del for **************
def capturar_datos():
    numeros = []  

    for i in range(0, 10, 2):
        print("Digite el Numero " + str(i+1) + ": ")
        numero = int(input())
        numeros.append(numero)

    return numeros
def procesar_datos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def mostrar_resultados(total):
    print("La sumatoria total es: " + str(total))


# ************* codigo principal *************
lista_numeros = capturar_datos()     
resultado = procesar_datos(lista_numeros)  
mostrar_resultados(resultado)        
