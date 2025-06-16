comentario = input("digite um comentario ")
posicoes = comentario.find("erro ")

if posicoes !=-1:
 print ("palavra'erro' encontrada na posicao ({posicoes})")
else:
 print("a palavra 'erro' nao encontrada ")

 print (" o tamanho do texto e de{len(comentario)} caracteres")