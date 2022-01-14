from random import randint
v = 0
while True:
    n = int(input("Digite um número: "))
    computador = randint(1, 10)
    resultado = (computador + n)
    pi = " "
    while pi not in "PI":
        pi = str(input("Escolha par ou ímpar: ")).strip().upper()[0]
        print(f"Você escolheu {pi}. A soma dos valores é {resultado}.")
    if pi == "P":
        if resultado % 2 == 0:
            print("Você venceu.")
            v += 1
            print("Vamos jogar novamente.")
        else:
            print("Você perdeu.")
            break

    elif pi == "I":
        if resultado % 2 == 1:
            print("Você venceu.")
            v += 1
            print("Vamos jogar novamente.")
        else:
            print("Você perdeu.")
            break
print(f"Game Over! Você venceu {v} vezes.")
