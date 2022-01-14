#Módulo random importando a função randint
from random import randint

#Váriavel composta do tipo Tupla.
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados {numeros}")

maior = 0
menor = 0

#Na estrutura de repetição (loop) for a classe enumerate enumera os valores de uma váriavel passada como parâmetro na classe.
for count, item in enumerate(numeros):
    if count == 0:
        maior = item
        menor = item
    else:
        if item > maior:
            maior = item
        elif item < menor:
            menor = item
print(f"O maior valor é: {maior}.")
print(f"O menor valor é: {menor}.")
print("=="*20)
print(f"O maior valor sorteado foi {max(numeros)}.")
print(f"O menor valor sorteado foi {min(numeros)}.")
