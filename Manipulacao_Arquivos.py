###############Leitura####################
#Mnatem o arquivo orginal intacto
 
#Abrindo o arquivo para leitura 
arq1 = open(r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/arquivo1.txt", "r") #r= read
#leitura do arquivo 
print (arq1.read())
print (arq1.tell())#conta numero de caracteres
print (arq1.seek(0,0))#retorna para o incio do arquivo
print(arq1.read(20)) #leitura de n caracteres

###########GRAVAÇÃO DE ARQUIVOS###########
#sobescreve o arquivo
arq2 = open (r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/arquivo2.txt","w") #w= write/somente para a escrita
arq2.write("Gravação teste")
arq2.close()#fechando o arquivo
arq2 = open(r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/arquivo2.txt","r")
print (arq2.read())
arq2 = open(r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/arquivo2.txt","a")
arq2.write(" Acrescenta sem sobrescrever")
arq2.close()
arq2 = open(r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/arquivo2.txt","r")
print(arq2.read())
 
##Dataset cidade de Chicago##
 
f = open (r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/salarios.csv",'r')
data = f.read()
rows = data.split ('/n')##split = dividir 
print (rows)

#divisao do arquivo em coluna
f = open (r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/salarios.csv",'r')
data = f.read()
rows = data.split ('/n')##split = dividir 
full_data = []
for row in rows:
    split_row=row.split(",")
    full_data.append(split_row)
print (full_data)

#contador de linhas do arquivo 
count = 0
for row in full_data:
 count += 1 
 
print (count)  
##contado o numero de colunas##
f = open (r"C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/salarios.csv",'r')
data = f.read()
rows = data.split ('/n')##split = dividir 
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data [0]
count = 0

for cplumn in first_row:
    count= count+1

import pandas as pd #imprtando pandas
arquivo = ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/salarios.csv")
df = pd.read_csv(arquivo)#abrindo o arquivo
print (df.head())#cabeça do arquivo#df = data frame
print (df['Position Title'].value_counts())

####ARQUIVOS TXT######
texto = "Cientista de Dados pode ser uma excelente alternativa de carreira./n"
texto = texto + "Esses profissionais precisam saber como programar em Python./n"
texto += "E, claro, devem ser proficientes em Data Science."

import os
#abrindo arquivo para grvação com pacote OS
arquivo = open(os.path.join("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/cientista.txt"),'w')

for palavra in texto.split():
    arquivo.write(palavra +' ')
    
arquivo.close ()

arquivo = open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/cientista.txt",'r')
conteudo = arquivo.read()
arquivo.close()

print (conteudo)

##EXPRESSÃO WITH####
#Executa o metodo close() automaticamente

#Sintaxe:
with open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/cientista.txt",'r') as arquivo:
    conteudo = arquivo.read()
    
print (len(conteudo))
print (conteudo)

with open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/cientista.txt",'w') as arquivo:
    arquivo.write(texto[:19])#filtro dos primeiros 19 caracteres
    arquivo.write('/n')
    arquivo.write(texto[28:66])
    
with open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/cientista.txt",'r') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)
   
###MANIPULAÇÃO DE ARQUIVOS CSV####
 
import csv
with open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/numeros.csv",'w') as arquivo:
  writer = csv.writer(arquivo) #cria o objeto de gravação
  #grava o arquivo linha a linha 
  writer.writerow(('nota1','nota2','nota3'))
  writer.writerow((63,87,92))
  writer.writerow((61,79,76))
  writer.writerow((72,64,91))
  
  
with open("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/numeros.csv",'r',encoding ='utf8', newline= '\r\n' ) as arquivo:
    #cria o obejto de leitura
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)
        
#geraçao de uma lista com dados do arquivo CSV

with open("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/numeros.csv",'r') as arquivo:
    leitor= csv.reader(arquivo)
    dados= list(leitor)

print (dados)

#imprimindo a partir da segunda linha:

for linha in dados[1:]:
    print(linha)

####MANIPULAÇÃO DE ARQUIVOS JSON #### 
#usa pares de chave valor similares a  dicionarios 
# Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c','Modula-3','lisp'],
              'users': 1000000}

#leitura do dicionario 
for k,v in dict_guido.items():
    print (k,v)
  
import json
print (json.dumps(dict_guido) )#conversão do dicionario para arquivo json
with open("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/dados.txt", 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))
#leitura dos arquivos
with open ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/dados.txt",'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto) #loads = carregar
    
print (dados)
 
#######extraçãop de arquivo web#######
import json
from urllib.request import urlopen
response = response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]
    
print (dados)

#,moostranmdo por chaves
print ('Titulo:', dados['title'])
print ('URL:', dados['url'])
print ('Duração', dados['duration'])
print ('TitulooNumero de visualizações', dados['stats_number_of_plays'])

#Copiando o conteudo de um arquivo para outro:

fonte ="C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/dados.json"
destino = "C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/dados.txt"

#duas formas: 

with open(fonte,'r') as infile:
    text = infile.read()
    with open (destino,'w') as outfile:
        outfile.write(text)
        
print(destino)
 
 # Leitura do arquivo txt
with open('C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/dados.txt','r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)    
    
print(dados)
  




