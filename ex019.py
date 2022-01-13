#Módulo random
import random

print("\033[1;36mQual aluna vai apagar o quadro?\033[m")
a1 = str(input("Aluna 1: "))
a2 = str(input("Aluna 2: "))
a3 = str(input("Aluna 3: "))
a4 = str(input("Aluna 4: "))
lista = [a1, a2, a3, a4]

#Sorteando a aluna da lista que apagará o quadro utilizando a função choice do módulo random.
print("Entre as alunas {}, {}, {}, {}, quem vai apagar o quadro é a aluna \033[1;32m{}\033[m".format(a1, a2, a3, a4, random.choice(lista)))
