from time import sleep
jogador = {}
partidas = list()
jogador["Nome"] = str(input("Nome do jogador: ").upper())
tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
print("+="*10)
for c in range(0, tot):
    partidas.append(int(input(f"Quantos gols o jogador {jogador['Nome']} fez na {c+1}º partida: ")))
jogador["Gols"] = partidas[:]

#A função sum soma todos valores númericos dentro de uma tupla, lista ou dicionário.
jogador["Total"] = sum(partidas)
print("=+"*10)
for k, v in jogador.items():
    print(f"{k} tem o valor {v}.")
print("+="*10)
print(f"O jogador {jogador['Nome']} jogou {tot} partidas.")
print("+="*10)
for pos, g in enumerate(jogador["Gols"]):
    print(f"Na {pos+1}º partida o jogador {jogador['Nome']} fez {g} gols.")
    sleep(0.5)
print("+="*10)
print(f"No total o jogador {jogador['Nome']} fez {jogador['Total']} gols.")
