###############Leitura####################
#Mnatem o arquivo orginal intacto

#Abrindo o arquivo para leitura 
arq1 = open(r"C:\Users\10391\Desktop\PythonDSA_conteudo\38-Cap06\arquivos\arquivo1.txt", "r") #r= read
#leitura do arquivo 
print (arq1.read())
print (arq1.tell())#conta numero de caracteres
print (arq1.seek(0,0))#retorna para o incio do arquivo
print(arq1.read(20)) #leitura de n caracteres

###########GRAVAÇÃO DE ARQUIVOS###########
#sobescreve o arquivo
arq2 = open (r"C:\Users\10391\Desktop\PythonDSA_conteudo\38-Cap06\arquivos\arquivo2.txt","w") #w= write/somente para a escrita
arq2.write("Gravação teste")
arq2.close()#fechando o arquivo
arq2 = open(r"C:\Users\10391\Desktop\PythonDSA_conteudo\38-Cap06\arquivos\arquivo2.txt","r")
print (arq2.read())
arq2 = open(r"C:\Users\10391\Desktop\PythonDSA_conteudo\38-Cap06\arquivos\arquivo2.txt","a")
arq2.write(" Acrescenta sem sobrescrever")
arq2.close()
arq2 = open(r"C:\Users\10391\Desktop\PythonDSA_conteudo\38-Cap06\arquivos\arquivo2.txt","r")
print(arq2.read())
