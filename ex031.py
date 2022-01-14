distância = float(input("\033[1;32mQuanto é a distância da sua viagem?\033[m "))
print("Você está prestes a começar uma viagem de \033[1;36m{}\033[mkm".format(distância))
if distância <= 200:
    t = distância * 0.50
    print("A tarifa da sua viagem é de \033[1;35m{:.2f}\033[mR$".format(t))
else:
    p = distância*0.45
    print("A tarifa da sua viagem é de \033[1;34m{:.2f}\033[mR$ \n\033[1;33mEm viagens acima de 200 km, a taxa de tarifa por cada quilometro percorrido é de 45 centavos.\033[m".format(p))

# preco = distância*0.50 if distância <= 200 else distância*0.45
# print("O preço da sua passagem será de {:.2f}R$".format(preco))
