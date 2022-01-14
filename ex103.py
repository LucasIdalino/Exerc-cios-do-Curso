def ficha(jog="<desconhecido>", gols=0):
    print(f"O jogador {jog} fez {gols} gol(s) no campeonato.")


a = str(input("Nome do jogador: "))
b = str(input("Número de gols: "))
if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == "":
    ficha(gols=b)
else:
    ficha(a, b)
