numeros = list()
while True:
    numeros.append(int(input("Digite um valor: ")))
    pergunta = str(input("Quer continuar? ")).upper()[0]
    if "N" in pergunta:
        break
print(f"Ao todo foram digitados {len(numeros)} números.")
numeros.sort(reverse=True)
print(f"Aqui estão os números em ordem decrescente: {numeros}.")
if 5 in numeros:
    print("O número 5 consta na lista.")
else:
    print("O número 5 não está na lista.")
