preço = float(input("Preço do produto? "))
print("""FORMAS DE PAGAMENTO
[1] A vista em dinheiro.
[2] À vista no cartão.
[3] 2x no cartão
[4] 3x no cartão""")

pagar = int(input("Escolha a opção de pagamento: "))

if pagar == 1:
    pagar = preço - (preço*10/100)
    print("A vista, em dinheiro, o produto terá 10% de desconto ficando por {:.2f}R$.".format(pagar))
elif pagar == 2:
    pagar = preço - (preço*5/100)
    print("A vista no cartão, o produto terá 5% de desconto ficando por {}".format(pagar))
elif pagar == 3:
    total = preço
    pagar = total/2
    print("Pagando 2x no cartão, o produto terá parcelas de R${:.2f} no preço normal.".format(pagar))
elif pagar == 4:
    total = preço
    parcel = preço + (preço*20/100)
    valor = int(input("Em quantas vezes?"))
    parce = parcel/valor
    print("Pagando em {}x no cartão, o produto terá um juros de 20%, ficando com parcelas de R${:.2f}, com valor "
          "total de R${:.2f}.".format(valor, parce, parcel))
else:
    total = preço
    print("OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.")

