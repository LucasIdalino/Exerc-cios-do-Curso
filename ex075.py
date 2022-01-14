a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
d = int(input("Digite o último número: "))
tupla = (a, b, c, d)
print(f"Você digitou os valores {tupla}.")

#No exemplo abaixo o método count() conta quantos valores existem dentro de uma váriavel aplicado no parãmetro do método.
print(f"O valor 9 apareceu {tupla.count(9)} vezes.")
if 3 in tupla:
    print(f"O número 3 apareceu na {tupla.index(3)+1}ª posição.")
else:
    print("O número 3 não apareceu em nenhuma posição.")

print("Os valores pares digitados foram:", end=" ")

#No exemplo abaixo "tupla[0]" o fatiamento isola um único valor dentro da tupla.
if tupla[0] % 2 == 0:
    print(tupla[0], end=" ")
if tupla[1] % 2 == 0:
    print(tupla[1], end=" ")
if tupla[2] % 2 == 0:
    print(tupla[2], end=" ")
if tupla[3] % 2 == 0:
    print(tupla[3], end=" ")
