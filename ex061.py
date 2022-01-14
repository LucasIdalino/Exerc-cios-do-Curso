pt = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
contador = 0
termo = pt
while contador < 10:
    print(f"{termo}", end=" ")
    termo += razão
    contador += 1
print("fim")
