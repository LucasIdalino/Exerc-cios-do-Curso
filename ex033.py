a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
# Verificando quem é menor
menor = a
if c < a and c < b:
    menor = c
if b < c and b < a:
    menor = b
if a < c and a < b:
    menor = a
# verificando quem é o maior
maior = a
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("\033[1;31mO menor valor digitado foi {}.\033[m".format(menor))
print("\033[1;32mO maior valor digitado foi {}.\033[m".format(maior))
