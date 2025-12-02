# ************* FUNCION CAPTURAR DATOS *************
def capturar_datos():
    print("Digite la cantidad de numeros para sumar: ")
    cantidad = int(input())  

    numeros = []  

    for i in range(cantidad): 
        print("Digite el Numero " + str(i+1) + ": ")
        numero = int(input())
        numeros.append(numero)

    return numeros

def procesar_datos(lista):
    suma = 0
    for num in lista:   
        suma = suma + num
    return suma

def mostrar_resultados(total):
    print("La sumatoria total es: " + str(total))


# ************* codigo principal *************
lista_numeros = capturar_datos()          
resultado = procesar_datos(lista_numeros) 
mostrar_resultados(resultado)             