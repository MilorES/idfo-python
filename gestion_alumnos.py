import calculadora as calc
# Se tendría que basar en m_diccionario

# Crear
def crear_alumno(d_alumnos, t_alumno): #  t_alumno es tupla
    if t_alumno is not None:
        d_alumnos[t_alumno[0]] = t_alumno[1]

# Eliminar                                            
def eliminar_alumno(d_alumnos, dni):
    if dni in d_alumnos:
        del d_alumnos[dni]

# Actualizar
def actualizar_alumno(d_alumnos, t_alumno):
        crear_alumno(d_alumnos, t_alumno)

# Recorrer "Mostrando por pantalla"
def mostrar_alumnos(d_alumnos):
    if len(d_alumnos) > 0:
        for alumno in d_alumnos.items():
            print(alumno[0],alumno[1], sep=' → ')
    else:
        print("No hay alumnos")

# Media
def calcular_media_alumnos(d_alumnos):
    sumatorio_notas = 0
    media = 0
    for alumno in d_alumnos.items():
        sumatorio_notas = calc.sumar(sumatorio_notas, alumno[1][1])
    else:
        media = calc.dividir(sumatorio_notas, len(d_alumnos))
    return media

def matricular_alumnos(d_aula,l_alumnos, l_dnis):
    for alumno in l_alumnos:
        dni = l_dnis.pop(0)
        crear_alumno(d_aula, (dni,alumno))  
