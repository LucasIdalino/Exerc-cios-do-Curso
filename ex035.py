print("-+-" * 10)
print("Analisador de triângulo")
print("-+-" * 10)

r1 = float(input("Digite o valor da reta 1: "))
r2 = float(input("Digite o valor da reta 2: "))
r3 = float(input("Digite o valor da reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[1;32mAs retas PODEM formar um triângulo.\033[m")
else:
    print("\033[1;31mAs retas NÃO PODEM formar um triângulo.\033[m")
