print("Analisador de triângulo.")

r1 = float(input("Digite a medida da reta 1: "))
r2 = float(input("Digite a medida da reta 2: "))
r3 = float(input("Digite a medida da reta 3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Essas retas podem formar um triângulo!")
    if r1 == r2 == r3:
        print("Este triângulo é EQUILÁTERO.")
    elif r1 != r2 != r3 != r1:
        print("Este triângulo será ESCALENO.")
    else:
        print("Este triânulo é ISÓSCELES.")
else:
    print("Essas retas não podem formar um triângulo.")
