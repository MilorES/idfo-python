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
otra_tupla = 1, 2, 3
tupla_cutre = 1,
print(type(otra_tupla))
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
except ValueError as e:
    print(f"Elemento no encontrado {e}")
except:
    print("Error desconico")
finally:
    print("Siempre me ejecuto")
    productos.remove("Quicos")

try:
    productos[11]
except IndexError as e:
    print(e)
except:
    print("Error desconocido")
productos.extend(["patata","lubina","Lengua de Vaca"])

# Diccionario

mi_diccionario = {1:'A', 2:'B'}
mi_diccionario_vacio = dict()
mi_otro_diccionario_vacio = {}
mi_diccionario_string = {"1":1,"2":3}

print('-' * 60) # Separador
print(mi_diccionario[1])
print(mi_diccionario_string["2"])

mi_diccionario[3] = 'C' # Alta
mi_diccionario_string["3"] = 3 # Alta

print("-" * 60) # Mostrar
for item in mi_diccionario.items():
    print(item[0], "se define como", item[1], sep=' / ')

del mi_diccionario[3] # Borrar
if(mi_diccionario.get(3) is None): # ¿Existe?
    print("No existe el elemento en el diccionario")

# Conjunto, elementos NO ORDENADOS y SIN REPETICIONES
print("-" * 30,"Conjuntos","-" * 30)
mi_conjunto_vacio = set()
mi_conjunto_creado_con_lista = set([1,2,3,4,4])
mi_conjunto_1 = {1,2,3,3}
mi_conjunto_2 = {1,2,4}

for item in mi_conjunto_1: # Mostrar
    print(item)

mi_conjunto_1.add(1)

print("Intersecion")
print(len(mi_conjunto_1.intersection(mi_conjunto_2)))
print(mi_conjunto_1.intersection(mi_conjunto_2))

print("Diferencia")
print(len(mi_conjunto_1.difference(mi_conjunto_2)))
print(mi_conjunto_1.difference(mi_conjunto_2))


print("Union")
print(len(mi_conjunto_1.union(mi_conjunto_2)))
print(mi_conjunto_1.union(mi_conjunto_2))
