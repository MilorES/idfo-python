# Dupla
restaurte = ("La Felicidad del Tapeo",972506550)
# Imprimir dupla y separadores
print(restaurte[0],restaurte[1],sep=": ")
print('-' * 60) # Separador
# Imprimir Tamaño
print(f"Tamaño tupla: {len(restaurte)}")
print('-' * 60) # Separador

# Tupla
una_tupla = tuple()
# Variable = Nombre, Telefono, Alta, Edad, Extrajero, Dinero
cliente = ("Jose Antonio", "636772756", True, 38, False, 18.3)
cliente2 = ("Juan Pablo","658975825",True, 41, True, 1000.05)
print('-' * 60) # Separador
# Imprimir último campo
print(cliente[-1])
# Imprimir con formato
print(f"Se llama {cliente2[0]} tiene el número de telefono {cliente2[1]}, Alta: {cliente2[2]} Edad: {cliente2[3]} Extranjero: {cliente2[4]} tiene {cliente2[5]} €")
print('-' * 60) # Separador
# Lista
una_lista = list()
nombres = ["Juan", "Maria", "Marcos", "Silvia"]
print(nombres[1])
print(nombres[-1])

productos = []
productos.append("Azucar")
productos.append("Pepinillos")
productos.append("Sal")
print('-' * 60) # Separador
# Imprimir ultimo producto
print(f"{productos[-1]}")
print("Antes de poner los insertar:",productos[1])
print('-' * 60) # Separador
# Añadir en la posicion y bajar el resto
productos.insert(1,"Quicos")
print("Despues de insertar:", productos[1])
productos.append("Sal")
print('-' * 60) # Separador
# Contar Apariciones
print("Cuantas de sal:", productos.count("Sal"))
print("Cuantas de zanahoria hay:", productos.count("Zanahoria"))
print('-' * 60) # Separador
# Cuantos elementos hay en lista
print("Cuantas elemtnos hay en la lista:", len(productos))
print('-' * 60) # Separador
# El lugar de la primera aparcion
print("Donde esta el elemto Pepinillos:", productos.index("Pepinillos"))
print('-' * 60) # Separador
# Borrar elemento
productos.remove("Sal")
print("Cuantas de sal:", productos.count("Sal"))
print('-' * 60) # Separador

# Eliminar
try:
    pos = productos.index("Sal")
    del productos[pos]
except ValueError:
    print("Elemento no encontrado")
productos.remove("Quicos")

