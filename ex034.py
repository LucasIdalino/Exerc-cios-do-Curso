salário = float(input("\033[1;36mQual o valor do seu salário?\033[m "))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print("Seu salário antigo era \033[1;31m{:.2f}\033[mR$, com o aumento vai ser \033[1;32m{:.2f}\033[mR$.".format(salário, novo))
