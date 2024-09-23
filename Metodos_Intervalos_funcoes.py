#Intervalo de valores com a Função Range## 
 
#loop para percorrer numeros de 1 a 10
for i in range (1,11): #o ultimo número é exclusivo, não é impresso
    print (i)

#definição de saltos 
for i in range (50,101,20): #primeiro numero da coleção, segundo numero, salto de numeros
    print (i) 

for i in range (0,-20,-5): #pode ser usada com valores negativos 
    print (i)

#usando o tamanho de uma lista na função range
lista = ['abacaxi','banana','morango','uva']
lista_tamanho = len (lista ) #atribuição da função len (tamanho) a uma variavel
for i in range (0,lista_tamanho):
    print (lista [i])

                                ##Métodos##
#tudo em python é objeto. Cada objeto tem métodos e atributos
#métodos são funções com ações que podem ser executadas nos objetos
#os objetos tem vários métodos a serem usados

lista = [1,2,3,4,100]

print (lista.append(100)) #adiciona elementos
print (lista.count(100)) #conta os elementos passados
print (dir (lista)) #mostra os atributos do objeto


                    ##Construção de funções##
#bloco de código que pode executar várias vezes fazendo a chamada
#quando a função faz parte de uma classe, ela é chamada de método

#definindo a função
def primeira_func ():
 nome = "bob"
 print ('hello %s' %(nome))

print (primeira_func())
 
#definindo função com parametro
def segundafunc (nome): #{1 parametro
 print ("Hello %s"% (nome))

#para chamar a função tem que passar o parametro
segundafunc('Leticia')

#função para imprimir numeros
def imprime_numeros (): #{ nenhum parametro
 for i in range (0,5):
  print ('número: ' + str(i))

imprime_numeros()

#Função para soma de numeros
def addnum (firstnum,secnum): #{dois parametros
 print ("Primeiro número: " + str(firstnum)) #str converte o nuemro p/ string para que ele possa ser concatenado com a string
 print ("Segundo número: " + str(secnum))
 print ("soma: ", firstnum + secnum)

addnum (45,45)

#Funções com nuemro variavel de parametros 
def print_var_info (arg1,*vartuple): 
    print ('parametro passado: ',arg1)
    for item in vartuple:
        print ('parametro passado: ',item)
    return;

print_var_info (10)
print_var_info (100,20,'morango') 