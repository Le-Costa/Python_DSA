##Condicionais####
'''
##condicional IF##
    #se algo acontecer faça algo
if 5>2:
    print ("Verdadeiro!") #{ nesse caso se não for verdadeiro, não acontecerá nada, por isso o uso do else:}

## if com else ###

if 5<2 :
    print ("verdadeiro")
else:
    print ("falso")

#inclusão de variaveis 
dia = 'terça'
if dia == 'segunda':
    print ("hoje fará sol!")
else: 
    print ("hoje irá chover")

#ELIF valida mais de uma condição 

if dia == 'segunda':
    print ('hoje fará sol')
elif dia == 'terça':
    print ("hoje vai chover")
else: 
    print ('Sem previsão para essa data')

#operadores lógicos#

- Operador **and** - Retorna True se ambas as declarações forem verdadeiras.
- Operador **or** - Retorna True se uma das declarações for verdadeira.
- Operador **not** - Inverte o resultado, retorna False se o resultado for True.


#AND
numero = 4 
if (numero > 2 ) and (numero %2 ==0):
    print ("Duas condições verdadeiras ")
else: 
    print ("Uma das condições é falsa ") 

#OR
numero = 4 
if (numero > 5 ) or(numero %2 == 0 ):
    print ("Uma das condições é verdadeira ")

#NOT 
if not (numero >5) and (numero %2 ==0):
    print ("As duas cndições são verdadeiras")
else: 
    print ("Uma das duas condições são falsas ")

    ##AND OR E NOT##
if (not (numero >5 )and (numero %2 == 0)) or (numero ==4):
  print ("As duas primeiras condições são verdadeiras ou a terceira é verdadeira. ")  

  ##INTRODUÇÃO DE PLACEHOLDERS##
disciplina = 'Data science'
nota_final = 90
semestre = 2

if disciplina == 'Data science' and nota_final >=80 and semestre != 1: 
    print ("Aprovado em %s com média final %r!" %(disciplina,nota_final))
else: 
    print ("Reprovado") '''

