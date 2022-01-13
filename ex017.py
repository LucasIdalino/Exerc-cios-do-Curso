#Utilizando a biblioteca hipotenusa do módulo math
from math import hypot

c_o = float(input("Qual o comprimento do cateto oposto? "))
c_a = float(input("Qual o comprimento do cateto adjacente? "))

#Calculando a hipotenusa.
h = hypot(c_o, c_a)
print('O comprimento da \033[7;31mhipotenusa\033[m é: \033[1;32m{:.2f}\033[mcm.'.format(h))
