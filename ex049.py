from time import sleep
n = int(input("Digite um número: "))

#Estrutura de repetição (loop) for.
for c in range(1, 11):
    sleep(0.5)
    print(f"{n} x {c} = {n*c}")
