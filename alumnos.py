alumnos = [    ("Juan",9.5),
                ("Maria",8.7),
                ("Carlos",8.7),
                ("Paco",7.1),
                ("Lucia", 6.8),
                ("Luis",4.7)
            ]
def calcular_media(l_alumnos):
    sumatorio_notas = 0
    media = 0.0
    for alumno in l_alumnos:
        #sumatorio_notas = sumatorio_notas + alumno[-1]
        sumatorio_notas += alumno[1]
    else:
        media = sumatorio_notas / len(l_alumnos)
    return media

resultado_media = calcular_media(alumnos)
print(round(resultado_media,2))

