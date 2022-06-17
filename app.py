# Asignar la variable nombre
nombre = 'Jose Antonio' #str
apellido = 'Rojo' #str
edad = 38 #int
nota = 8.54 #float
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
print(f'Hola, me llamo {nombre} y tengo {edad} años')

bAprobado = nota >= 5

if bAprobado:
    print('Has aprobado')
else:
    print('No has aprobado')

'''
Uso de la variable edad
para evaluar algo
'''

if edad == 10:
    print('Curso primaria')
elif edad == 15:
    print("Curso ESO")
else:
    print("Otros")

# Resultados Oposicion
experiencia_laboral = 11
puntosextras = 10 if experiencia_laboral >= 10 else 0 #Expresion if, one-liner
if puntosextras == 10:
    print("Tienes puntuacion adicional")
else:
    print("No tienes puntuacion adicional")

#Strings
primer_caracter = nombre_completo[0]
print("Primer caracter", primer_caracter, sep=':')
print("Str tiene un longitud:", len(nombre_completo))
ultimo_caracter = nombre_completo[-1] #Forma Pythoniana
print("Ultimo caracter", ultimo_caracter, sep=':')

pos_espacio = nombre_completo.index(' ')
print(f'Posicion del espacio {pos_espacio}')
print(nombre_completo[0:pos_espacio])
print(nombre_completo.split(" ")[0])
print(nombre_completo[pos_espacio + 1:])
print(nombre_completo.split(" ")[2])
print(nombre_completo[2:-2])

#nombre_completo recorrido
for caracter in nombre_completo:
    print('Car:',caracter.upper())

i = 3
while i < len(nombre_completo):
    print('Car:',nombre_completo[i].upper())
    i = i + 4
