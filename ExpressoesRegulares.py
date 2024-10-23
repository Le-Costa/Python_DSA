#Usadas para manipulação de strings, usados para combinar ou encontrar sequencias de caracteres
with open(r"C:/Users/10391/Desktop/arquivos txt/banco de dados.txt",'r')as arquivo:
    conteudo=arquivo.read()
    
##Conta quantos vezes o carcater aparece    
import re
resultado=len(re.findall('a',conteudo))
print (resultado)


with open(r"C:/Users/10391/Desktop/arquivos txt/banco de dados.txt",'r')as arquivo:
    conteudo=arquivo.read()
 #expressão para extrair a palvra que aparece após a plavra indicada   
resultado = re.findall(r'identifica (\w+)',conteudo)#\w codigo de palavra
print(resultado[0])#é retornado em forma de lista

#Nota: O r antes da string que representa a expressão regular em Python é usado 
# para indicar que a string é uma string literal raw. Isso significa que as barras 
# invertidas (\) não são interpretadas como caracteres de escape, mas são incluídas
# na expressão regular como parte do padrão.

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."
# Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(emails)
