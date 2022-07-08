import ficheros 
# from ficheros import funcion as alias

if __name__ == "__main__":
    pass

ficheros.escribir_datos("Hola sesion python", "data.txt")
print("*" * 30, "Mostrando error.txt", "*" * 30)
ficheros.leer_datos("error.txt")
#ficheros.leer_datos("data.txt")
ficheros.escribir_datos("Primera linea", "data.txt")
ficheros.modificar_datos("Añado una linea", "data.txt")
ficheros.modificar_datos("Añado otra linea", "data.txt")
#ficheros.leer_datos("data.txt")
lineas = ficheros.leer_datos_v2("data.txt")

numero_total_caracteres = ficheros.procesar_datos(lineas)
print("*" * 30, "Número caracteres data.txt ", "*" * 30)
print(numero_total_caracteres)

# Variante: fichero nuevo, que en cada linea muestra los caracteres de la misma

ficheros.nuevo("countcharlinea.txt")
listaData = ficheros.leer_datos_v2("data.txt")
#texto_nuevo = ""
for lin in listaData:    
    ficheros.modificar_datos(ficheros.procesar_dato(lin),"countcharlinea.txt")
print("*" * 30, "Mostrando data.txt", "*" * 30)
ficheros.leer_datos("data.txt")
print("*" * 30, " Número caractres linea data.txt","*" * 30)
ficheros.leer_datos("countcharlinea.txt")
