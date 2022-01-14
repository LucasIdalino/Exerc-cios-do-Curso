from random import randint
from time import sleep

numeros = []


def sorteia(lst):
    for n in range(0, 5):
        lst.append(randint(1, 50))
    print(f"Sorteado {len(numeros)} da lista:", end=" ", flush=True)
    for c in numeros:
        print(c, end=" ", flush=True)
        sleep(0.5)
    print("Pronto!")


soma = []


def somapar(valor):
    for c in valor:
        if c % 2 == 0:
            soma.append(c)
    print(f"Somando os valores pares de {numeros}, temos {sum(soma)}.")


a = numeros
sorteia(a)
somapar(a)
