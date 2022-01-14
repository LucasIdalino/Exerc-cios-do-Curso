matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para ({l}, {c}): "))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
print(f'Na matriz, a soma dos números pares é: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da coluna 2 é {scol}.")
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}.")

