#import gestion_alumnos as gest_al
from gestion_alumnos import matricular_alumnos, \
                            calcular_media_alumnos, \
                            mostrar_alumnos, \
                            actualizar_alumno, \
                            eliminar_alumno

# Fuente 1
alumnos = [    ("Juan",9.5),
                ("Maria",8.7),
                ("Carlos",8.7),
                ("Paco",7.1)
            ]

# Fuente 2
dnis = ["111H","222Z","333C","444C"]

aula = dict()

#gest_al.matricular_alumnos(aula,alumnos,dnis) # Si usas el import directo
matricular_alumnos(aula,alumnos,dnis)

def informe_calificaciones(d_aula):
    print("Lista de alumnos:\n")
    mostrar_alumnos(d_aula)
    print('\nFin lista de alumnis.')

def revisar_nota(aula,t_dni,f_nota):
    print("DEBUG", aula[t_dni][0])
    print("DEBUG", f_nota)
    actualizar_alumno(aula, (t_dni,(aula[t_dni][0],f_nota)))

if len(aula):
    #resultado_media = gest_al.calcular_media_alumnos(aula) # Si usas el import directo
    resultado_media = calcular_media_alumnos(aula)
    print(round(resultado_media,2))

informe_calificaciones(aula)
revisar_nota(aula, "444C", 8)
informe_calificaciones(aula)
eliminar_alumno(aula,"444C")
informe_calificaciones(aula)