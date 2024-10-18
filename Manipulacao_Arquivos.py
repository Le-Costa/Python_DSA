###############Leitura####################
#Mnatem o arquivo orginal intacto
'''
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
'''
##Dataset cidade de Chicago##
'''
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
'''
import pandas as pd #imprtando pandas
arquivo = ("C:/Users/10391/Desktop/PythonDSA_conteudo/38-Cap06/arquivos/salarios.csv")
df = pd.read_csv(arquivo)#abrindo o arquivo
print (df.head())#cabeça do arquivo#df = data frame
print (df['Position Title'].value_counts())

 


