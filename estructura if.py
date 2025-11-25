#******Estrcutrua del if, elif, else***********
#******zona de funciones*********
def tomar_numero():
    numero = int(input("escriba un numero: "))
    
    if numero > 0:
     print("su numero es positivo.")
     
    elif numero==0:
        print("su numero es neutro.")
        
    else:
        print("su numero es negativo.")
    
    
def decir_mensaje (numero):
        mensaje = str(numero)
        return 
    
def imprimir_mensaje(mensaje):
     print(mensaje)    
     
     #******codigo principal**********  
     
numero = tomar_numero()
dato_mensaje = decir_mensaje(numero)
imprimir_mensaje = (dato_mensaje)


     
     
        
    