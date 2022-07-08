def nuevo(nombre_fichero):
    with open(nombre_fichero, "w") as f:
        f.write("")
        # no es necesario porque el with te lo cierra que es un bloque f.close 

def escribir_datos(data, nombre_fichero):
    with open(nombre_fichero, "w") as f:
        f.write(f"{data}\n")
        # no es necesario porque el with te lo cierra que es un bloque f.close 

def modificar_datos(data, nombre_fichero):
    try:
        with open(nombre_fichero, "a") as f:
            f.write(f"{data}\n")
    except:
        print("Error: Fichero no encontrado")

def leer_datos(nombre_fichero):
    try:
        with open(nombre_fichero, "r") as f:
            print(f.read())
    except:
        print("Error: Fichero no encontrado")

def leer_datos_v2(nombre_fichero:str) -> list:
    try:
        with open(nombre_fichero, "r") as f:
            return f.readlines()
    except:
        print("Error: Fichero no encontrado")

def procesar_dato(data:str) -> int:
    return len(data.strip())

def procesar_datos(data:list):
    num_caracteres = 0
    if data is not None:
        if type(data) is list:
            for linea in data:
                num_caracteres += procesar_dato(linea)
    return num_caracteres

'''
escribir_datos("Hola sesion python", "data.txt")
leer_datos("error.txt")
leer_datos("data.txt")
escribir_datos("Primera linea", "data.txt")
modificar_datos("Añado una linea", "data.txt")
modificar_datos("Añado otra linea", "data.txt")
leer_datos("data.txt")
lineas = leer_datos_v2("data.txt")

numero_total_caracteres = procesar_datos(lineas)
print(numero_total_caracteres)
'''