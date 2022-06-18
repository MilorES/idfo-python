# Ennvio de paquetería, El AMAZON con ALMA!
def crear_paquete(identificador, contenido, destino):
    return (identificador, contenido, destino) # Tupla

def enviar_paquete(t_paquete):
    print (f"Enviando {t_paquete[1]} hacia {t_paquete[2]}")

def enviar_paquetes_urgentes(c_paquetes):
    for paquete in c_paquetes:
        enviar_paquete(paquete)

if __name__ == "__main__":
    paquete_1 = crear_paquete(1,"Consola XBOX","Albacete")
    paquete_2 = crear_paquete(2,"Jabón de lavadora","Barcelona")
    paquete_3 = crear_paquete(3,"Remo de piragua","Luego")
    # enviar_paquete(paquete_1)

    paquetes = set([paquete_1, paquete_2, paquete_3]) # Un cojunto que se le da un lista
    paquetes_urgentes = set([paquete_1, paquete_3]) # Un cojunto que se le da un lista
    paquetes_normales = set([paquete_2]) # Un cojunto que se le da un lista que solo tiene un elemento

    enviar_paquetes_urgentes(paquetes.difference(paquetes_normales))
