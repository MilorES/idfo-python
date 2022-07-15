'''
imc = peso / altura*altura
Underweight imc < 18.5
Normal imc > 18.5 %% 25 < imc
Overweight imc > 25 a imc < 30
Obesity imc > 30
'''
print("Introduce el peso:")
peso = float(input())
print("Introduce la altura")
altura = float(input())
#imc = peso / (altura * altura)
imc = peso / altura**2
print(imc)
if imc < 18.5:
    print("Underweight")
elif imc >= 18.5 and imc < 25:
    print("normal")
elif imc >= 25 and imc < 30:
    print("Overweight")
else:
    print("Obesity")
