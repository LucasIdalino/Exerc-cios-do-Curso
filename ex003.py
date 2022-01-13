n = int(input("Digite um número:"))
n2 = int(input("Digite um segundo número:"))

#Somando o valor de duas váriaveis.
soma = n+n2

#Imprimindo o resultado da soma colorizado pelo padrão ANSI.
print("A soma de \033[1;32m{}\033[m mais \033[1;35m{}\033[m é \033[1;33m{}\033[m!".format(n, n2, soma))
