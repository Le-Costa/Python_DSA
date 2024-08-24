""""
numeros = list(range(1, 101))
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(div4)
"""

### ("CALCULO DE AREA DE PARALEOGRAMA###
'''
print("Calculador de area de paralelogrma")

base = float(input("Insira o comprimento a base:"))
altura = float(input("Insira a altura:"))

area = base * altura
print("Area do paralelograma: ", area)
'''

## CALCULADORA SIMPLES##

num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))
ope = input("Qual a operação? (+,-,*,/)")

if ope == "+":
    resultado = num1+num2
    print("O resultado é: ", resultado)

elif ope == "-":
    resultado = num1-num2
    print("O resultado é: ", resultado)

elif ope == "*":
    resultado = num1*num2
    print("O resultado é: ", resultado)
elif ope == "/":
    resultado = num1/num2
    print("O resultado é: ", resultado)
else:
    print("Operação inválida!")
