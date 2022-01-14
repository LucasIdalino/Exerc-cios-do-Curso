#Váriável composta do tipo lista. list()
listanum = list()
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor na posição {c+1}: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print("*="*20)
print(f"O maior número foi {maior} e está na posição:", end=" ")
for c, v in enumerate(listanum):
    if v == maior:
        print(f"{c+1}...", end=" ")
print()

print(f"O menor número foi {menor} e está na posição:", end=" ")
for c, v in enumerate(listanum):
    if v == menor:
        print(f"{c+1}...", end=" ")
print()

