import pickle

def guardar_usuarios(nombre_fichero:str,l_usuarios:list):
    
    fichero = open(nombre_fichero,'wb')
    pickle.dump(l_usuarios, fichero)
    fichero.close()

def obtener_usuarios(nombre_fichero:str) -> list:
    l_usuarios = None
    try:
        with open(nombre_fichero, 'rb') as f:
            l_usuarios = pickle.load(f)   
    except FileNotFoundError as exc:
        print(exc)
    except Exception as exc:
        print(f"Error I/O {exc}")
    return l_usuarios

if __name__ == "__main__":
    s_nombre_fichero = "usuarios.bin"
    usuarios = ['matias','juana','marcos']
    guardar_usuarios(s_nombre_fichero, usuarios)
    usuarios = obtener_usuarios(s_nombre_fichero)
    if(usuarios is not None):
        print(usuarios)
