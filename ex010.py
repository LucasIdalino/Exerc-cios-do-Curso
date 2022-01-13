d = float(input("Quantos reais você tem? R$"))

#conversão
cambio = d/5.37
cor = {"azul":"\033[1;34m",
       "verde":"\033[1;32m"}
print("Com R$ \033[1;34m{:.2f}\033[m, você pode comprar US$\033[1;32m{:.2f}\033[m.".format(d, cambio))
