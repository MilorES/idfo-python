from multiprocessing.reduction import duplicate


numeros = range(40)

datos = list(map(lambda x : x * 3, numeros))
print(datos)

masdatos = filter(lambda x : x % 2 == 0, numeros)
print(list(masdatos))

duplicar = lambda x : x * 2
print(duplicar(7))
