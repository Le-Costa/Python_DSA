#Modulo é um arquivo que contem cod python e pode ser importado em outros arquivos python.Usado p compartilhar funções,classes e variaveis entre arquivos
#pacote é uma coleção de módulos organizados em uam estrutura de diretórios.Ele permite a divisão de um app em multiplos módulos, o que facilita a manutenção e o desenvolvimento.

import numpy #importação do pacote
(dir (numpy))#verifica todos os métodos e atributos disponiveis no pacote

print(numpy.sqrt(25))#calculo de raiz quadrada
#from numpy import sqrt #importação apenas do método

print(numpy.sqrt(13))

import random #pacote randoonização 
random.choice(['abacate','banana','laranja'])
print (random.sample(range(100),10)) #retorna numeros aleatorios
import statistics #calculo de estatisticas
dados = [2.75,1.75,1.25,0.25,0.5,1.25,3.5]

print (statistics.mean(dados))#calcula a media do conjunto de dados
print (statistics.median(dados))#extrai a mediana

