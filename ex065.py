pergunta = "S"
soma = 0
cont = 0
maior = 0
menor = 0
while pergunta in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    pergunta = str(input("Quer continuar? ")).upper().strip()[0]
    média = soma/cont
print(f"Você digitou {cont} números e a média foi {média:.2f}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
