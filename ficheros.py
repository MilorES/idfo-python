def escribir_datos(data, nombre_fichero):
    with open(nombre_fichero, "w") as f:
        f.write(data)
        # no es necesario porque el with te lo cierra que es un bloque f.close 

def leer_datos(nombre_fichero):
    try:
        with open(nombre_fichero, "r") as f:
            print(f.read())
    except:
        print("Error: Fichero no encontrado")

def modificar_datos(data, nombre_fichero):
    try:
        with open(nombre_fichero, "a") as f:
            f.write(f"\n{data}")
    except:
        print("Error: Fichero no encontrado")

escribir_datos("Hola sesion python", "data.txt")
leer_datos("error.txt")
leer_datos("data.txt")
escribir_datos("Primera linea", "data.txt")
modificar_datos("Añado una linea la final", "data.txt")
leer_datos("data.txt")
