'''
numeros = list(range(1, 101))
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
print(div4)


### ("CALCULO DE AREA DE PARALEOGRAMA###

print("Calculador de area de paralelogrma")

base = float(input("Insira o comprimento a base:"))
altura = float(input("Insira a altura:"))

area = base * altura
print("Area do paralelograma: ", area)


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

# CONVERSÃO DE NUMEROS#

float(9)
int(6.0)
int(6.3)

# HEXADECIMAL PARA BINARIO#
hex(394)
bin(17)


# FUNÇOES#
# retorna o valor absoluto

abs(-8)

# Arredonda os numeros
round(3.1548657, 4)

# Potencia

pow(5, 3)


## variaveis##

# atribuindo valor

var1 = 3
# impressao
print(var1)

# declaração multipla

pessoa1, pessoa2, pessoa3 = "Le", "Wagner", "Nadia"


print(pessoa1)
print(pessoa2)
print(pessoa3)

fruta1 = fruta2 = fruta3 = "Pessego"

print(fruta2)


# CONCATENAÇÃO DE VARIAVEL#

TextoAd = input("Insira um texto: ")

nome = "Leticia"
sobrenome = "Costa"

FullName = nome + " " + sobrenome + " " + TextoAd

print(FullName)
'''

# STRING E INDEXAÇÃO#

# Pode se usar aspas simples ou duplas

# QUEBRA DE LINHA#

print('teste \n quebra \n de \n linha')

# indexação de string#

# atribuindo valor

x = 'Primeira string'

print(x)

# indexação começa com 0

print(x[0])

print(x[5])

# UM SLICING COMEÇA PELA POSIÇÃO X ATÉ O FIM DA STR
#: no fim, retorna tudo até  o fim da str
print(x[3:])

#: no começo retorna tudo até indice x

print(x[:7])

# indexação negativa lede tras pra frente

print(x[:-1])
