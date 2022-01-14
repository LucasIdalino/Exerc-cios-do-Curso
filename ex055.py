maior = 0
menor = 0
for c in range(1, 7):
    peso = int(input(f"O peso da {c}º pessoa: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso lido foi {maior}Kg.")
print(f"O menor peso lido foi {menor}Kg.")
