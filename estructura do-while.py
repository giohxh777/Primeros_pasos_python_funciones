#*******estructura del Do-while*******
#*******zona de funciones*******
def capturar_datos():
    
 print("digite la letra 'A' para actualizar sistema")
 print("digite la letra 'E' para eliminar catalogo")
 print("digite la letra 'C' para para crear producto")
 print("digite la letra 'S' para salir del programa")
 
 letra= input("seleccione una opcion")
 return letra.upper()

def analizar_datos (opcion):
 if opcion == 'A':
  return("se actualizo sistema")
 elif opcion == 'E':
  return("se elimino catalogo")
 elif opcion == 'C':
  return("se creo un producto")
 elif opcion == 'S':
  return"s"
  
 else:
    return "la informacion no es valida"

def imprimir_datos(resultado):
        print("\n>",resultado,"\n")

     
#*******codigo principal********
while True:
  opcion=capturar_datos()
  resultado = analizar_datos(opcion)
if resultado=="S":
    print("\nfinalizar el programa con exito. \n")
    
mostrar_datos(resultado)

print ("el do-while a finalizado")

     
     
  
 
 

 

