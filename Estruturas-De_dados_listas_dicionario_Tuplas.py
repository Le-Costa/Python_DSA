# criando listas
# Listas ficam entre colchetes, tuplas entre parenteses

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

lista_a = [[1, 2, 3], [56, 78, 99], [87, 89, 54]]
print(lista_a)

lista_b = [['aaa', 'bbbbb'], ['hkkhdhd', 'okjg']]
print(lista_b)
