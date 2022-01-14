numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input("Digite um valor: ")))
    pergunta = str(input("Quer continuar? [S/N]")).upper()[0]
    if "N" in pergunta:
        break
for p, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"A lista com todos o números: {numeros}.")
print(f"A lista com os números pares: {pares}.")
print(f"A lista com os números ímpares: {impares}.")
