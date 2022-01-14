
print("Qual base de conversão você quer escolher?")

n = int(input("Digite um número: "))
print("""Escolha uma das bases para conversão:
[1] converter em binário
[2] converter em octal
[3] converter em hexadécimal""")
escolha = int(input("Escolha sua opção: "))
if escolha == 1:
    print("{} convertido para binário é {}.".format(n, bin(n)[2:]))
elif escolha == 2:
    print("{} convertido para octal é {}".format(n, oct(n)[2:]))
elif escolha == 3:
    print("{} convertido para hexadécimal é {}.".format(n, hex(n)[2:]))
else:
    print("Opção inválida. Tente novamente.")
