from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter.tix import Tree


nombre_completo = "Felipe Sanchez"
copia_nombre_completo = nombre_completo[:]

print("Nombre Completo:", nombre_completo)
print("Nombre Completo (copia):", copia_nombre_completo)

# copia_nombre_completo = "pepinotres"

print("ID_NC:",id(nombre_completo))
print("ID_CNC",id(copia_nombre_completo))

# Sin Optimizar
a = 1
b = 2
print(id(a))
print(id(b))

# Optimizado
b = 1 
print(id(a))
print(id(b))

# nombre_completo[0] = "H" # Inmutable
nombre_completo = 1

clientes = list()
# Tupla // dupla con dos elementos // limite 22?
cliente = ("Juan", "972056897", True) # Estructura de datos
print(type(cliente))
clientes.append(cliente)

clientes.append(("Pedro", "972058978", None)) # comparar is None

print("Num Clientes", len(clientes))

pedro_esta_graduada = clientes[-1][-1]
print(pedro_esta_graduada)
if pedro_esta_graduada:
    print("Esta graduada")
else:
    print("No esta graduada")

for client in clientes:
    if client[-1]:
        print(client[0], "esta graduado")
    else:
        print(client[0], "no esta graduado")

def cliente_graduado(cliente):
    return cliente[-1] == True

juan = clientes[0]
if cliente_graduado(juan):
    print("Juan Graduado")

maria = clientes[-1]
if cliente_graduado(maria):
    print("Maria Graduado")

'''
# Crear funcion de añadir clientes
def cliente_nuevo_anade(cliente, lista):
    lista.append(cliente)
    #return lista
'''

# Crear funcion de listar clientes
def cliente_listar(lista):
    print ( '-' * 60)
    for l in lista:
        print(l[0])

# Crear funcion de añadir clientes
def cliente_nuevo_anade(nombre, telefono, graduado, lista):
    lista.append((nombre, telefono, graduado))
    #return lista

# Crear funcion de borrar clientes
def cliente_eliminar(l, nombre_cliente):
    for c in l:
        if c[0] == nombre_cliente:
            l.remove(c)
            break # Mejor un while

# Falta la funcion para borrar todo

# Invocar Funcion
cliente_nuevo_anade("Josep", "972118978", False, clientes)
print(clientes[-1])
# nuevo_cliente = ("Ruben", "978526489", True)
# cliente_nuevo_anade(nuevo_cliente, clientes)

cliente_listar(clientes)
cliente_eliminar(clientes, "Juan")
cliente_listar(clientes)
