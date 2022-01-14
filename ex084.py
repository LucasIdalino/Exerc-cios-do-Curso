pessoa = list()
galera = list()
maior = menor = 0
while True:
    pessoa.append(str(input("Nome: ")).upper())
    pessoa.append(float(input("Peso: ")))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    pergunta = str(input("Quer continuar? [S/N]")).upper()[0]
    if "N" in pergunta:
        break
print(f"Ao todo temos {len(galera)} cadastradas.")
print(f"O maior peso foi de {maior}Kg. Peso de", end=" ")
for p in galera:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
print()
print(f"O menor peso foi de {menor}Kg. O peso de", end=" ")
for p in galera:
    if p[1] == menor:
        print(f"{p[0]}", end=" ")
print()
