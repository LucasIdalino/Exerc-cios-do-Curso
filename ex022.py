#Valor da variável sem espaços no ínicio e fim.
nome = str(input("Seu nome: ")).strip()

#Valor da variável em letras maiúscula.
print("Maiúscula:", nome.upper(), "\033[1;32m<--\033[m")

#Valor da variável em letras minúsculas.
print("Minúscula:", nome.lower(), "\033[1;32m<--\033[m")

#Contando quantas letras tem o valor da várialvel nome sem espaços.
print("Meu nome tem:", len(nome)-nome.count(" "), "\033[1;32m<--\033[m")
# print("Meu primeiro nome tem:", nome.find(" "))


# print("Seu primeiro tem {} letras".format(nome.find(" ")))
separa = nome.split()
print("Meu primeiro nome tem:", len(separa[0]), "\033[1;32m<--\033[m")
