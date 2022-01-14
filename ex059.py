from time import sleep
n = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    opção = int(input("Qual opção você quer escolher: "))
    if opção == 1:
        some = n + n2
        print("A soma de {} + {} é {}".format(n, n2, some))
    elif opção == 2:
        multiplicação = n * n2
        print("O resultado da multiplicação de {} x {} é {}".format(n, n2, multiplicação))
    elif opção == 3:
        if n > n2:
            maior = n
        else:
            maior = n2
        print("Entre {} e {}, o maior número é {}.".format(n, n2, maior))
    elif opção == 4:
        print("Informe o número novamente.")
        n = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente.")
    print("=+=" * 10)
    sleep(1)
sleep(2)
print("Fim do programa.")
