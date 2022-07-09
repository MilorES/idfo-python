def dividir(x, y):
    return x / y

print(dividir(10,4))

#lambda
division = lambda x , y : x / y
res = division(10,4)
print("Division lambda" + str(res))

#lista
lista = [1,2,3,4,5]

#lista comprehension
lista2 = [item * 3 for item in lista]
print(lista2)
