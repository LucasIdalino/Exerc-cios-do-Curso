preco = float(input("\033[1;33mQual o preço?\033[m: "))

#Calculando desconto.
novo_preco = preco - (preco * 5/100)
print("O produto que custava {:.2f}R$, na promoção com desconto de 5% fica por: \033[1;36m{:.2f}\033[mR$".format(preco, novo_preco))
