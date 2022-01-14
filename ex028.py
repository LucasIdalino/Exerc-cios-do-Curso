#Módulo random importando a função randint
#Módulo time importando a função sleep
from random import randint
from time import sleep

print("\033[1;36m*=*\033[m" * 20)
print("\033[1;35mTENTE ACERTAR O NÚMERO QUE ESCOLHI\033[m")
print("\033[1;36m*-*\033[m" * 10)

#Palpite aleatório do computador usando a função .randint() entre os números de 0 até 5
computador = randint(0, 5)

#Palpite do jogador
jogador = int(input("\033[1;34mTente advinhar qual número escolhi\033[m: "))

#A função .sleep() que conta os segundos aplicado dentro parâmetro para imprimir a mensagem
print("PROCESSANDO"), sleep(3)

#Condição if
if jogador == computador:
    print("\033[1;32mVocê venceu. Eu escolhi {} e você escolheu {}.\033[m".format(computador, jogador))
else:
    print("\033[1;31mEu venci, escolhi o número {}!\033[m".format(computador))
print("*-*" * 10)
