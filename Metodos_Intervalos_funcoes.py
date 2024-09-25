 # Intervalo de valores com a Função Range##

# loop para percorrer numeros de 1 a 10
for i in range(1, 11):  # o ultimo número é exclusivo, não é impresso
    print(i)

# definição de saltos
for i in range(50, 101, 20):  # primeiro numero da coleção, segundo numero, salto de numeros
    print(i)

for i in range(0, -20, -5):  # pode ser usada com valores negativos
    print(i)

# usando o tamanho de uma lista na função range
lista = ['abacaxi', 'banana', 'morango', 'uva']
lista_tamanho = len(lista)  # atribuição da função len (tamanho) a uma variavel
for i in range(0, lista_tamanho):
    print(lista[i])

    ## Métodos##
# tudo em python é objeto. Cada objeto tem métodos e atributos
# métodos são funções com ações que podem ser executadas nos objetos
# os objetos tem vários métodos a serem usados

lista = [1, 2, 3, 4, 100]

print(lista.append(100))  # adiciona elementos
print(lista.count(100))  # conta os elementos passados
print(dir(lista))  # mostra os atributos do objeto

## Construção de funções##
# bloco de código que pode executar várias vezes fazendo a chamada
# quando a função faz parte de uma classe, ela é chamada de método

# definindo a função


def primeira_func():
    nome = "bob"
    print('hello %s' % (nome))


print(primeira_func())

# definindo função com parametro


def segundafunc(nome):  # {1 parametro
    print("Hello %s" % (nome))


# para chamar a função tem que passar o parametro
segundafunc('Leticia')

# função para imprimir numeros


def imprime_numeros():  # { nenhum parametro
    for i in range(0, 5):
        print('número: ' + str(i))


imprime_numeros()

# Função para soma de numeros


def addnum(firstnum, secnum):  # {dois parametros
    # str converte o nuemro p/ string para que ele possa ser concatenado com a string
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secnum))
    print("soma: ", firstnum + secnum)


addnum(45, 45)

# Funções com nuemro variavel de parametros


def print_var_info(arg1, *vartuple):
    print('parametro passado: ', arg1)
    for item in vartuple:
        print('parametro passado: ', item)
    return


print_var_info(10)
print_var_info(100, 20, 'morango')

# escopo de variavel local e global
# variaveis globais estão fora de funções e podemser acessadas em qualquer parte do código
# variaveis locais só existem dentro de uma função e só podem ser acessadas por tal

# revisão Funções bult in
# são funções prontas
print(abs(56))  # retorna o valor absoluto
print(bool(10))  # valor boleano
print(int(4.325678))  # retorna o valor inteiro
print(str(13))  # converte numero para string
print(float(5))  # converte para decimal
print(len([1, 2, 3, 4, 5, 6]))  # retorna tamanho
array = [1, 2, 3, 4]
print(max(array))  # maior numero da variavel
print(min(array))  # menor numero da variavel
print("soma: ", sum(array))
 
##SPLIT DE DADOS###

def split_string_plavras (text):
    return text.split (" ")

texto = 'esta função será bastante util para separar grnades volumes de dados'
print (split_string_plavras(texto))

# se pode atribuir o output de uma função p/ um avariavel
token = (split_string_plavras(texto))
print (token)

def split_string_letras (text):
     texto = text.upper () #passa todas as letras da variavel para maiusculo
     for letra in texto:#percorre as letras da variavel 
          print (letra)# printa cada letra do loop

print (split_string_letras(texto))

        ###Expressão Lambda####

# definindo um afunção em 3 linhas de código
def potencia (num):
     resultado = num **2
     return resultado 

print (potencia(5))

#definindo a função em 2 linhas de código 
def potencia (num):
     return num **2

print (potencia (5))

#definindo em uma linha de codigo 
def potencia (num): return num **2

print (potencia(5))

#definindo uma expresao lambda ( anonima)- cria a função em tempo de execução
potencia = lambda num: num**2

print (potencia(5))

#retorna apenas numero pares 
par = lambda x: x%2==0

print (par (4))

            #LIST COMPREHENSION AND DICT COMPREHENSION### Loop dentro de lista
#[expressaõ for item in iterable if consição ==true]
#LC  que imprime os numeros ate 10 
print ([x for x in range (10)])

lista_numeros=[x for x in range (10) if x<5]
print (lista_numeros)

#lista de frutas 
frutas = [ 'banana','limao','abacate','manga']

nova_lista = []

#loop tradicional buscando as palavras com letra m

for x in frutas:
    if 'm' in x:
        nova_lista.append(x)

print (nova_lista)

# loop em LC

nova_lista = [x for x in frutas if 'm' in x]
print (nova_lista)

                    ###Dict conmprhension##

alunos = {'bob':68, 'leticia':19}

alunos_status = {k:v for (k,v) in alunos.items()}
print (alunos_status)