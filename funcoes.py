###FUNÇÃO MAP###
 
#Aplica uma determinada função a cada elemento de uma estrutura de dados iteravel
#EXEMPLO:
def potencia(x): #definição de função
    return x**2

numeros = [1,2,3,4,5,6]
quadrado = list(map(potencia,numeros)) #lê-se = map aplica potencia, a cada item da lista de numeros
#lista esta convertendo os resultados em uma lista
print(quadrado)

#Função 1= recebe a temperatura e retorna em fahrenheit
def fah (t):
    return((float(9)/5)*t+32)

#função 2= recbe a temp e rertorna em celsius

def celsius (t):
    return((float(5)/9)*(t-32))

temp = [0,22.5,40,100]
#aplicando a função a caeda elemento daa lista de temperaturas
#função map retorna um iterator

print(list (map(fah,temp)))#map aplica a função fah na lista temp

#usando loop para imprimir o resultado da função
for tempe in map (fah,temp):
    print(tempe)

#usando lambda, não ha necessidade de definir uma função
print (list(map(lambda x: (5.0/9)*(x-32),temp)))

#somando oos elementos de duas listas:
a = [1,2,3,4]
b = [5,6,7,8]

print(list(map(lambda x,y:x+y,a,b)))#o retorno sera uma lista
#lê-se: x,y serão x+y aplicado a a e b

########FUNCAO REDUCE##########
#Reduz uma lista de elementos a  um unico valor, somando os valores e retornando um apenas
from functools import reduce
#EXEMPLO: Fazer a reducao de 4 numeros
lista = [ 47,11,42,13] #Lista de numeros 

def soma (a,b):
    x=a+b
    return x

#Usando reduce com uma função e uma lista. A função retorna o valor máximo
print (reduce(soma,lista))

#usando reduce coom lambda
print (reduce(lambda x,y:x+y,lista))

#Atribuindo uma função a uma variavel 
#Lê-se: lambda receba a e b, se a for > b retorna a senão b
max_find = lambda a,b: a if (a>b) else b

type(max_find)

#reduzindo a lista ate o valor maximo, atraves da função lambda
print (reduce(max_find,lista))

#######FUNCAO FILTER###########
#aplica um filtro a um objeto interavel

def verificaPar (num):
    if num %2==0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

#A função filter retorna o que for verdadeiro para a função verificaPar
#Ela retorna um iterador então tem que converter em lista

print (list(filter(verificaPar,lista)))

#usando com lambda
print(list(filter(lambda x: x%2==0,lista)))
#verificando apenas numeros maiores que 8
print(list(filter(lambda num: num>8,lista)))

####FUNCAO ZIP####
#Agrupa varios elementos de multiplas estruturas de dados e pode ser convertido em outra estrutura de dados

#Duas listas
x = [1,2,3]
y = [4,5,6]

#unindo as listas. Retorna um iterator
zip(x,y)

#Covertendo para lista
print(list(zip(x,y)))#retorno [(1, 4), (2, 5), (3, 6)]
#retorna uma lista de tuplas
#junta o 1° elemento c/ o 1° elemntoo, o 2° c/ 2° e assim vai

#Atençãoo ao juntar sequencias c/ numeros diferentes de elementos
#Se a função não conseguir combinar, ela vai descartar
#exemplo:
list(zip('ABCD', 'xy'))#[('A', 'x'), ('B', 'y')]

#duas lista c/ numero de elementos diferentes
a = [1,2,3]
b = [4,5,6,7,8]

print(list(zip(a,b))) #[(1, 4), (2, 5), (3, 6)]

# Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}
# A função list, combina as chaves dos dicionarios por padrao
print(list(zip(d1,d2)))#[('a', 'c'), ('b', 'd')]

#para união dos valores, é necessário chamar o método values
#Nesse caso ele uniu a chave do 1° elemento com o valor do 1° elemento 
print(list(zip(d1, d2.values()))) #[('a', 4), ('b', 5)]

# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp


print (trocaValores(d1, d2)) #{'a': 4, 'b': 5}
 

#####FUNCAO ENUMERATE######
#enumera uma estrutura
#retorna um iterador
 
# Criando uma lista
seq = ['a','b','c']
#retorna os valores da lista com seus respectivos indices
#retorna pares de indice e valor
print(list(enumerate(seq))) #[(0, 'a'), (1, 'b'), (2, 'c')]

#imprimindo os valores de uma lsita com indices
for indice,valor in enumerate(seq):
    print(indice,valor)

for indice,valor in enumerate(seq):
    if indice>=2:
        break
    else:
        print(valor)
        
#Pode se usar em strings, listas,tupla, range etc...









