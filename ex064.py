n = 0
i = 1
cont = 0
n = int(input("Digite um número: "))
while n != 999:
    n = int(input("Digite um número: "))
    i += n
    cont += 1
    k = i - 1000
print(f"Ao todo {cont} valores foram digitados, a soma de todos essas valores é {k}.")
