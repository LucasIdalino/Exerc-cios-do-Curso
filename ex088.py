from random import randint
from time import sleep
jogo = list()
jogos = list()
print("MEGASENA")
cartela = int(input("Quantos jogos você quer? "))
tot = 1
while tot <= cartela:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    
    #O método .clear() apaga todos valores de uma lista.
    jogo.clear()
    tot += 1
print(f" Sorteando {cartela} jogos.")
for v, l in enumerate(jogos):
    print(f"Jogo {v+1}: {l}")
    sleep(1)
print("Boa sorte")

