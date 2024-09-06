# criando listas
# Listas ficam entre colchetes, tuplas entre parenteses
'''
lista_1 = ['arroz,feijão,macarrão']  # lista com UMA string

print(lista_1)
print(type(lista_1))


# listas com strings independentes

lista_2 = ['cereja', 'maça', 'pera', 'tomate']  # lista DE strings
print(lista_2)

# lista mista#

lista_3 = [20, 546, 'string dentro da lista']
print(lista_3)

### ATRIBUINDO VALORES DA LISTA A UMA VARIAVEL###

item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

print(item1, item2, item3)

# ATUALIZAR ITEM DA LISTA

print(lista_2)
lista_2[3] = 'chocolate'
print(lista_2)

# deletar item da lista
print(lista_2)
del lista_2[0]
print(lista_2)
print(lista_1)

###### LISTA DE LISTAS#######
# As lista de listas são as matrizes

lista_a = [[1, 2, 3], [56, 78, 99], [87, 89, 54]]
print(lista_a)

lista_b = [['aaa', 'bbbbb'], ['hkkhdhd', 'okjg']]
print(lista_b)

# Atribuição de um item da lista a uma variavel

a = lista_a[0]  # a recebeu a lista que esta no indice 0 (1,2,3)
b = a[0]  # b recebeu o indice 0 de a (1)

valor1 = lista_b[1]
print(valor1[0])

salada = [['tomate', 'abacate'],
         [ 'rucula', 'alface', 'agriao'],
        ['cenoura', 'brocolis']]
frutas = salada[0]
folhas = salada[1]
vegetais = salada[2]

print(frutas[1])
print(folhas[2])
print(vegetais[0])


## OPERAÇÃO COM LISTAS###

lista_num = [[0, 1, 2], [20, 25, 30], [22, 24, 26, 28]]
print(lista_num)

a = lista_num[1][0]  # 20
b = lista_num[2][3]  # 28
print(a, b)

soma = lista_num[2][0] + 10  # 32

print(soma)

d = 10
e = d * lista_num[2][2]
print(e)
'''
## CONCATENAÇÃO DE LISTAS###
frutas = [['amora', 'tomate', 'uva'], ['maça', 'pera', 'ameixa']]
vegetais = [['alface', 'rucula']]

salada = frutas + vegetais

print(salada)  # Não concatena como uma lista só

# Para sair uma unica lista
vegetais = [item for sublista in (frutas + vegetais)for item in sublista]
print(vegetais)

# FUNÇÕES BULT IN

print(len(vegetais))  # retorna o comprimento da lista

numeros = [2, 4, 6, 8, 10]
print(max(numeros))  # numero maximo da lista

print(min(numeros))  # numero minimo da lista

### COPIA DOS ITENS DE UMA LISTA PRA OUTRA#
nova_lista = []  # lista vazia

for item in numeros:
    nova_lista.append(item)

# colocar itens no final
cidades = ['Recife', 'Manaus', 'Salvador']

cidades.extend(['fortaleza', 'palmas'])
print("cidades extend", cidades)

print(cidades.index('Recife'))  # localiza o index de determinado item

# Para inserir usar função insert

cidades.insert(2, 110)  # indice,valor a adicionar
print('inseert', cidades)

cidades.reverse()  # reverte a lista
print('reverse', cidades)

cidades.sort  # ordena a lista
print('sort:', cidades)
