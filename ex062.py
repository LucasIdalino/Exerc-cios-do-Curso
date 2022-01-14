primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))
termo = primeiro
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(f"{termo}", end=" ")
        termo += razão
        c += 1
    print(" - PAUSA")
    mais = int(input("Quantos termos a mais você quer mostrar? "))
print("Fim")
