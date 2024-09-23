## Condicionais####

## condicional IF##
# se algo acontecer faça algo
if 5 > 2:
    # { nesse caso se não for verdadeiro, não acontecerá nada, por isso o uso do else:}
    print("Verdadeiro!")

## if com else ###

if 5 < 2:
    print("verdadeiro")
else:
    print("falso")

# inclusão de variaveis
dia = 'terça'
if dia == 'segunda':
    print("hoje fará sol!")
else:
    print("hoje irá chover")

# ELIF valida mais de uma condição

if dia == 'segunda':
    print('hoje fará sol')
elif dia == 'terça':
    print("hoje vai chover")
else:
    print('Sem previsão para essa data')

# operadores lógicos#
'''
- Operador ** and ** - Retorna True se ambas as declarações forem verdadeiras.
- Operador ** or ** - Retorna True se uma das declarações for verdadeira.
- Operador ** not ** - Inverte o resultado, retorna False se o resultado for True.
'''

# AND
numero = 4
if (numero > 2) and (numero % 2 == 0):
    print("Duas condições verdadeiras ")
else:
    print("Uma das condições é falsa ")

# OR
numero = 4
if (numero > 5) or (numero % 2 == 0):
    print("Uma das condições é verdadeira ")

# NOT
if not (numero > 5) and (numero % 2 == 0):
    print("As duas cndições são verdadeiras")
else:
    print("Uma das duas condições são falsas ")

    ## AND OR E NOT##
if (not (numero > 5) and (numero % 2 == 0)) or (numero == 4):
    print("As duas primeiras condições são verdadeiras ou a terceira é verdadeira. ")

    ## INTRODUÇÃO DE PLACEHOLDERS##
disciplina = 'Data science'
nota_final = 90
semestre = 2

if disciplina == 'Data science' and nota_final >= 80 and semestre != 1:
    print("Aprovado em %s com média final %r!" % (disciplina, nota_final))
else:
    print("Reprovado")

##### LOOP FOR ####
tp = (2, 3, 4)
for i in tp:
    print(i)

frutas = ['amora', 'tomate', 'uva']
for i in frutas:
    print(i)

for contador in range(0, 5):  # conjunção de elementos#
    print(contador)

# impressaõ de numero pares em uma lista# #Loop com condição#

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('numeros pares: ')
for num in numeros:
    if num % 2 == 0:
        print(num)

# range com incrementeo: (primeiro numero, segundo numero, incremento).
for i in range(0, 101, 2):
    # Nesse caso vai percorrer de 0 a 101 pulando de dois em dois
    print(i)

for caracter in "Estou usando o vscode ":
    print(caracter)


# LOOPS ANINHADOS#

# loop aninhado
lista1 = [0, 1, 2, 3, 4]
lista2 = [1, 2, 3,]

# loop externo

for elemento_lista1 in lista1:
    for elemento_lista2 in lista2:
        print('\n', elemento_lista1 * elemento_lista2)
    print('-----')


# o numero 47 aparece nas duas listas?
lista3 = [10, 16, 24, 39, 47]
lista4 = [32, 89, 47, 76, 12]

for elemento_lista3 in lista3:
    for elemento_lista4 in lista4:
        if elemento_lista3 == 47 and elemento_lista4 == 47:

            print("O número 47 aparece nas duas listas")


# soma dos numros pares da lisat3 com os da lista4
soma = 0

for lista in [lista3, lista4]:

    for num in lista:

        if num % 2 == 0:
            soma += num  # sinal de atribuição +=#
print("A soma dos números pares é = a:", soma)


# Aquele é diferente deste #
soma = 0
for num in lista3 + lista4:
    if num % 2 == 0:
        soma += num  # sinal de atribuição +=#
print("A soma dos números pares é = a:", soma)


matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0

for linha in matriz:
    for num in linha:
        if num > maior_numero:
            maior_numero = num
print("maior nuemro: ", maior_numero)


## LOOP WHILE##

# a condição tem que ser verdadeira pelo menos uma vez
# Ela tem que parar de ser verdadeira em algum momento, se não da um loop infinito

valor = 0
while valor < 5:
    print(valor)
    valor = valor + 1

# Pode se usar else com while
x = 0
while x < 5:
    print("X nesta iteração :", x)
    print("x ainda é menor que 10, somando 1 a x")
    x += 1
else:
    print("loop concluido")
print(x)

# PASS, BREAKE E CONTINUE#

var1 = 0
while var1 < 5:  # primeiro loop acontecerá enquanto a var1 for menor que 5
    if var1 == 4:  # depois de checar se é menor que 5 verifica se é igual 4
        break       # se for igual a 4 o brek para o loop
    else:           # se não for igual a 4 passa para o comando seguinte
        pass
    print(var1)
    var1 = var1 + 1

for letra in "Estou usando o zzz vscode":
    if letra == 'z':  # Condição para continuar o código e ignorar
        continue  # Desconsidera o a letra#
    print(letra)
