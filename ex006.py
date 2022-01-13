x = int(input("Digite um número: "))

#Calcula o dobro do valor da varável.
print("O dobro de \033[1;31m{}\033[m é \033[1;32m{}\033[m".format(x, (x * 2)))

#Calcula o triplo e a raiz quadrada da variável.
print("O triplo de \033[1;31m{}\033[m é \033[1;32m{}\033[m. \nE a raiz quadrada de \033[1;31m{}\033[m é \033[1;32m{}\033[m".format(x, (x * 3), x, int(x ** (1 / 2))))

print("Obrigado!")
