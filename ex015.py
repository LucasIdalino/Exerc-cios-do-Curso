km = int(input("\033[7;31;40mQuantos quilometros percorridos?\033[m: "))
d = float(input("Quantos dias?: "))

#Calculando o valor do alguel de carros. Calculando os dias por 60 e a quilometragem por 0.15
aluguel_carro = (d*60)+(km*0.15)

print("O total a pagar é de \033[1;36m{:.2f}\033[mR$".format(aluguel_carro))
