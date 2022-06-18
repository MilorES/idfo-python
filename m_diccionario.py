
#Alta
def diccionario_alta (clave, valor, diccionario):
    diccionario[clave] = valor
    return diccionario

# Baja
def diccionario_baja(clave, diccionario):
    del diccionario[clave]
    return diccionario

# Actualizar
def diccionario_actualizar(clave, valor, diccionario):
    return diccionario_alta(clave, valor, diccionario)

# Recorrer "Mostrando por pantalla"
def diccionario_recorrer(diccionario):
    for item in diccionario.items():
        print(item[0],item[1], sep=':')

# Crear Modulo de diccionario que pueda Alta, Baja, Actualizar y Recorrer 