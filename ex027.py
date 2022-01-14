#A função .strip() elimina os espaços do início e fim da palavra.
#A função .split() elimina os espaços entre as palavras de uma frase.
nome = str(input("Digite seu nome:")).strip().split()

#Uso do fatiamento de strings.
print("Primeiro nome é:", nome[0])

#Método len() conta quantas letras tem o valor de uma váriavel string.
print("Seu último nome é:", nome[len(nome)-1])
