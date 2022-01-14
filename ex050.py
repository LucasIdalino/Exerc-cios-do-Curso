soma = cont = 0
for c in range(1, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f"Ao todo, tem {cont} números pares. A soma dos pares é {soma}.")
