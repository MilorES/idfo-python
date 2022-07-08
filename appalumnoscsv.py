import ficheros as files

def procesar_alumnos(l_alumnos):
    """
    id,nombre,apellido,curso,notafinal
    splis -> ["id","nombre","apellido","curso","notafinal"]
    """
    res_alumnos = [] # ¿Tupla?
    for alumno in l_alumnos:
        info_alumno = alumno.split(',')
        res_alumnos.append((info_alumno[0],info_alumno[1],info_alumno[-1]))
    return res_alumnos

def calcular_media_alumnos(l_alumnos:list) -> float:
    # Controlar division 0
    sumatorio_notas = 0.0
    if type(l_alumnos) is list:
        for alumnos in l_alumnos:
            sumatorio_notas += float(alumnos[-1])
            print(sumatorio_notas)
    else:
        sumatorio_notas = -1
    return sumatorio_notas / len(l_alumnos)

if __name__ == "__main__":
    lst_alumnos = files.leer_datos_v2("alumnos.csv") # Coga la lista desde la pos 1 "Segunda" al -1 "final"
    alumnos_procesados = procesar_alumnos(lst_alumnos[1:]) #[("id","nombre","notafinal"),(.,.,.),(.,.,.)]
    print(f"Media de clase: {calcular_media_alumnos(alumnos_procesados)}")
