#Números Pares:
#Crie uma lista com os números pares de 0 a 20 usando lista comprehension.

pares = [x for x in range (0,21) if x %2==0 ]
print ('pares= ', pares)
#Gere uma lista dos quadrados dos números de 1 a 10.
quadrados = [x*x for x in range (1,11)]
print ('quadrados = ', quadrados)
#Dada uma lista de palavras ["gato", "sol", "lua", "computador", "céu"], 
# crie uma nova lista contendo apenas as palavras com mais de 3 letras.
animais= ["gato", "sol", "lua", "computador", "céu"]
animais2 = [x for x in animais if len(x)>3] ###### não esta funcionando 
print ('animais = ', animais2) 

#A partir da lista de palavras ["Python", "Data", "Machine", "Learning", "AI"], 
#crie uma lista com a primeira letra de cada palavra.
dados= ["Python", "Data", "Machine", "Learning", "AI"],
dados2 = [ x[0] for x in dados]
print ('primeira letra= ', dados2)

#Crie uma lista com os números de 1 a 50 que são divisíveis por 3.
divisiveis = [ x for x in range (1,51) if x%3 ==0]
print ('divisiveis por 3:', divisiveis )

#Inverter Palavras:
#Dada uma lista de palavras ["banana", "maçã", "uva", "abacaxi"],
# use lista comprehension para gerar uma nova lista com cada palavra invertida.

frutas= ["banana", "maçã", "uva", "abacaxi"]
inverso = [x[::-1] for x in frutas ]
print ( 'inverso: ', inverso )

#Dada uma lista de palavras 
# ["python", "comprehension", "exercise", "list", "basic"], 
# crie uma nova lista contendo o comprimento de cada palavra.

lista = ["python", "comprehension", "exercise", "list", "basic"]
comprimento = [len(x) for x in lista]
print ('comprimento: ',comprimento)

#Dada a lista ["hello", "world", "python", "code", "list", "comprehension"],
#filtre apenas as palavras que têm mais de 5 letras e converta-as para maiúsculas.

lista= ["hello", "world", "python", "code", "list", "comprehension"]
filtro = [palavra.upper() for palavra in lista if len(palavra)>5 ]
print ("Mais que 5 letras: ", filtro)

#A partir da lista ["dog", "cat", "bird"], crie uma lista de strings no formato "<número>: <palavra>",
#onde o número representa a posição da palavra na lista.

animais= ["dog", "cat", "bird"]
posicao = [f"{i + 1}: {animal}" for i, animal in enumerate(animais)]
print ("Posições: ", posicao)
