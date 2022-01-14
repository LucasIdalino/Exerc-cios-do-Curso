from time import sleep
jogador = {}
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: ").upper())
    tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols o jogador {jogador['Nome']} fez na {c+1}º partida: ")))
    jogador["Gols"] = partidas[:]
    jogador["Total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        pergunta = str(input("Adicionar mais um jogador? [S/N] ")).upper()[0]
        if pergunta in "SN":
            break
        print("Por favor, responda sim ou não.")
    if pergunta == "N":
        break
print("cod", end=" ")

#O método keys mostra as chaves de um dicionário.
for c in jogador.keys():
    print(f"{c:<15}", end=" ")
print()
print("+="*10)
for k, v in enumerate(time):
    print(f"{k:>3}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("+="*20)
while True:
    busca = int(input("Qual jogador você quer ver os dados? "))
    if busca == 999:
        break
    if busca > len(time):
        print("Jogador não encontrado. Tente novamente.")
    else:
        print(f"Dados do jogador {time[busca]['Nome']}")
        for k, g in enumerate(time[busca]["Gols"]):
            print(f"Na partida {k+1} fez {g} gol(s).")
print("Volte Sempre.")
