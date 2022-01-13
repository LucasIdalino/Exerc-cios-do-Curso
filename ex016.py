import math
n = float(input("\033[4;31mDigite um número\033[m: "))

#Conhecendo o número quebrado de um número flutuante.
print("O número {}, tem sua parte inteira \033[1;33m{}\033[m.".format(n, math.trunc(n)))
