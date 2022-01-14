n = int(input("Digite um número: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print("\033[31m", end="")
    else:
        print("\033[32m", end="")
    print(c, end=" ")
print(" ")
print(f"\033[mO número {n} é divido {tot} vezes.")
if tot == 2:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")
