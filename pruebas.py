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
