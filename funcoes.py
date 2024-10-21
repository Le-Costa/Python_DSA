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
