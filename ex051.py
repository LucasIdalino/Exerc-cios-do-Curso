pt = int(input("Qual o primeiro termo? "))
r = int(input("Qual a razão? "))
soma = pt + (10-1)*r
for c in range(pt, soma + r, r):
    print(c, end=" ")
