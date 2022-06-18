dicccionario = {
    "Python" : "Es un lenguaje de programacion interpretado flexible",
    "C++" : "Es el C con Objetos",
    "PHP" : "Lenguaje interpreado para web",
    "Javascript" : "Un truño"
}

print(dicccionario["Python"])

# Alta
dicccionario["PHP"] = "Es un lenguaje de back-end para creacion de HTML y javascript"
print(dicccionario["PHP"])
dicccionario["Java"] = "Lenguaje de donde salio el C#"

print("-" * 60)
for item in dicccionario.items():
    print(item[0], "se define como", item[1], sep='-.-')

# Baja
del dicccionario["PHP"]

print("-" * 60)
for item in dicccionario.items():    
    print(item[0], "se define como", item[1], sep='-.-')

# Crear Modulo de diccionario que pueda Alta, Baja, Actualizar y Recorrer 

# conjunto : Agrupación de elementos NO ORDENADOS y SIN REPETICIONES

conjunto_a = set() # conjuntoA = {}
conjunto_a.add(1)
conjunto_a.add(2)
conjunto_a.add(3)
conjunto_a.add(4)
conjunto_a.add(9)

conjunto_b = {1,2,7,8}
conjunto_l = set([1,2,3,4,4,4,4,5]) # Crear un conjunto desde una LISTA
print("*" * 60)
print(conjunto_b)
print(type(conjunto_b))

print("*" * 60)
for item in conjunto_a:
    print(item)

conjunto_a.add(4)

print("*" * 60)
for item in conjunto_a:
    print(item)

print("*" * 60)
print(len(conjunto_a.intersection(conjunto_b)))
print(conjunto_a.intersection(conjunto_b))

print("*" * 60)
print(len(conjunto_a.difference(conjunto_b)))
print(conjunto_a.difference(conjunto_b))


print("*" * 60)
print(len(conjunto_a.union(conjunto_b)))
print(conjunto_a.union(conjunto_b))

# Iteración 2 sobre funciones
print("Iteración 2 sobre funciones")
def calcular (x, y, z = 1): # Argumentos obligatorios a la izquierda y los opciones a la derecha
    return x / y - z

print(calcular(10, 5, 7))

print(calcular(10, 5))

print(calcular(y=10, x = 5))
