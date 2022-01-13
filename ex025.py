#A função .upper() transforma as letras da palavra em maiúsculas. 
#A função .strip() elimina os espaços do início e fim da palavra.
nome = str(input("Digite seu nome completo: ")).upper().strip()

#Mostra em valor booleano se o valor da variável tem ou não a palavra "silva".
print("silva" in nome.lower())
