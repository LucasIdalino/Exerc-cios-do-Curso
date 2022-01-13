n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))

#Faz a soma das variáveis e depois divide o resultado da soma por 3.
cálculo = (n1+n2+n3)/3

print("A média de fulano é \033[1;32m{:.1f}\033[m".format(cálculo))
