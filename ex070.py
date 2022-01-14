preço1000 = 0
menorpreço = 0
soma = 0
barato = " "
cont = 0
while True:
    nome = str(input("Nome do produto: "))
    preço = int(input("Preço R$"))
    cont += 1
    if preço > 1000:
        preço1000 += 1
        soma += preço
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        barato = nome
        soma += preço
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? ")).upper().strip()[0]
    if continuar == "N":
        break
soma += preço
print("DADOS DAS COMPRAS")
print(f"No total suas compras deram R${soma}")
print(f"Temos {preço1000} produtos custando mais de R$ 1000.")
print(f"O produto mais barato é {barato}, custando R${menorpreço}")
