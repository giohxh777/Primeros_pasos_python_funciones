#********zona de funciones****
#palabra_clave + nombre_funcion(verbo) + parametros(adjetivos)
def capturar_nombre():
   nombre_usuario = input("escriba el nombre del cliente:")
   return nombre_usuario
def capturar_rol() :
    rol_usuario = input("escriba su rol:")
    return rol_usuario

def capturar_hora():
 hora = int (input("escriba la hora"))
 if hora > 0  and hora < 12:
     print ("buenos dias")
 elif hora >= 12 and hora < 18 :
    print("buenas tardes")
 elif hora >= 18 and hora < 24 :
     print("buenas noches")
 else:
     print("hora incorrecta")
    
     
 


def hacer_saludo(nombre_usuario, rol_usuario):
    mensaje = " hola " + nombre_usuario + " rol: " + rol_usuario 
    return mensaje
def imprimir_mensaje(mensaje) :
    print(mensaje)
    #******zona de codigo principal*****
dato_nombre = capturar_nombre()
rol_usuario = capturar_rol()
dato_hora = capturar_hora()
mensaje = hacer_saludo(dato_nombre, rol_usuario)
imprimir_mensaje(mensaje) 

    