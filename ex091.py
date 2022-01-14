from random import randint
from time import sleep
from operator import itemgetter
jogadores = {"jogador1": randint(1, 6),
             "jogador2": randint(1, 6),
             "jogador3": randint(1, 6),
             "jogador4": randint(1, 6)}
print("-="*5, "SORTEANDO JOGADAS", "-="*5)

#O método .items() exibi as chaves e o valores de um dicionário.
for k, v in jogadores.items():

    print(f"O {k} tirou {v} no dado.")
    sleep(1)

#No código abaixo classe itemgetter busca um valor dentro de uma tupla, lista ou dicionário. Neste caso, o parâmetro key está tomando como alvo os valores do dicionário "jogadores".

#O reverse, mostra os valores de uma tupla, lista ou dicionários em ordem reversa.
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f"-="*5, "Ranking dos Jogadores", "-="*5)
for p, j in enumerate(ranking):
    print(f"{p+1}º lugar: {j[0]} com {j[1]} pontos.")
    sleep(1)
