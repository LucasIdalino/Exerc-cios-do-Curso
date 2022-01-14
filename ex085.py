numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f"Todos os valores digitados: {numeros}.")
print(f"Os valores pares foram: {numeros[0]}.")
print(f"Os valores ímpares foram: {numeros[1]}.")
