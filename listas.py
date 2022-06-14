# Listas

"Juan Perez" # Colección de caracteres

#Colección de nombres Juan, Maria, Marcos, Silvia
nombres = ["Juan", "Maria", "Marcos", "Silvia"]

for nombre in nombres:
    print("Nombre", nombre, sep=":")

for nombre in nombres:
    print("Primer Caracter", nombre[0], "Ultimo Caracter", nombre[-1], sep=":")
print("Tipo de datos de la variable nombres",type(nombres))

#Ver todos los nombres en mayusculas
for nombre in nombres:
    print(nombre[:1].upper())

bolsa_playa = [] # Lista Vacia
#Toalla, Cervezas, Parasol, Crema, Chancletas, Flotador Pato
bolsa_playa.append("Toalla")
bolsa_playa.append("Cervezas")
bolsa_playa.append("Parasol")
bolsa_playa.append("Crema")
bolsa_playa.append("Chancletas")
bolsa_playa.append("Flotador Pato")

print("Cuantas toallas:", bolsa_playa.count('Toalla'))

# Añadir toalla
bolsa_playa.append("Toalla")
print(len(bolsa_playa))
print("Cuantas toallas:", bolsa_playa.count('Toalla'))

bolsa_playa.insert(0, 'Cervezas')
print("Cuantas cervezas:", bolsa_playa.count('Cervezas'))

cervezas_primera_posicion = bolsa_playa[0] == 'Cervezas'
if(cervezas_primera_posicion):
    print("La cervezaz esta en la primera posicion, viva la cerveza")

hay_cervezas = bolsa_playa.index('Cervezas')  > -1

if(hay_cervezas):
    print("Tenemos cervezas, vamos a la playa")
else:
    print("Pilla la cervezas y para la playa")

print('-' * 60) # Separador

for cosas in bolsa_playa:
    print(cosas)

#Quitar Cervezas 
print("Numeros de Cervezas", bolsa_playa.count('Cervezas'))
while(bolsa_playa.count('Cervezas') > 0):
    bolsa_playa.remove('Cervezas')
print("Numeros de Cervezas", bolsa_playa.count('Cervezas'))

#Estamos en la playa
''' 
Sacamos las toallas
Sacamos la crema
'''

pos_toalla = bolsa_playa.index('Toalla')
if pos_toalla > -1:
    cosaExtraida = bolsa_playa.pop(pos_toalla)
cosaExtraida = bolsa_playa.pop(bolsa_playa.index('Crema'))

bolsa_playa.count('Pepino')

item_a_eliminar = input("Que quieres elimnar de la bosa?")
if len(item_a_eliminar) > 0:
    bolsa_playa.remove(item_a_eliminar)

for cosa in bolsa_playa:
    print(cosa)
