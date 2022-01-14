valor_casa = float(input("Qual o valor da casa?: "))
salario = float(input(("Salário do comprador?: ")))
anos = int(input("Em quantos anos o comprador vai pagar?: "))

pm = (valor_casa/(anos*12))

minimo = (salario*30/100)

print("Para pagar uma casa de R$\033[1;33m{:.2f}\033[m em \033[1;36m{}\033[m anos.".format(valor_casa, anos), end=" ")
print("A prestação será de R$\033[1;33m{:.2f}\033[m.".format(pm))
if pm <= minimo:
    print("Seu empréstimo foi \033[1;32maprovado.\033[m")
else:
    print("Seu empréstimo foi \033[1;31mnegado\033[m.")
