##Condicionais####

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
