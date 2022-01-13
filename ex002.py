#Usando o padrão de Escape ANSI para por cor no terminal.
nome = input ("\033[1;31mQual o seu nome?")
print("Bem vindo,\033[1;32m{}!\033[m". format(nome))
