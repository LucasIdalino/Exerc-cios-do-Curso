frase = str(input("Digite uma frase: ")).strip().upper()
separar = frase.split()

#A função .join() junta palavras.
juntar = "".join(separar)
inverso = ""
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
print(juntar, inverso)
if juntar == inverso:
    print("Está frase é um palíndromo.")
else:
    print("Está frase não é um palíndromo.")

