#Utilizando o módulo math e suas funções: radians, sin, cos, tan
from math import radians, sin, cos, tan

#Sabendo o seno, cosseno e a tangente de um ângulo
angulo = float(input("Digite um ângulo: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o seno de \033[1;32m{:.2f}\033[m".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o cosseno de \033[1;33m{:.2f}\033[m".format(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem a tangente de \033[1;34m{:.2f}\033[m".format(angulo, tangente))
