n = int(input("Digite um número para saber o fatorial: "))
contador = n
fatorial = 1
print(f"{n}! =", end=" ")
while contador > 0:
    print(f"{contador}", end=" ")
    print("x" if contador > 1 else "=", end=" ")
    fatorial *= contador
    contador -= 1
print(fatorial)
