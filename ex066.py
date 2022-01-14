soma = cont = 0
#Estrutura de repetição (loop) while.
while True:
    n = int(input("Digite um número. 999 encerra o programa: "))
    if n == 999:
        #O comando break interrompe a repetição.
        break
    soma += n
    cont += 1
print(f"Você digitou {cont} número(s). A soma de todos os números é {soma}.")
