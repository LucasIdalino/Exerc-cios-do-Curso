#Tipo de váriavel composta: Tupla
números = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
           "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")
while True:
    pergunta = int(input("Digite um número entre 0 e 20: "))
    if 0 <= pergunta <= 20:
        palavra = números[pergunta]
        break
    print("Digite novamente.", end=" ")
#palavra = números[pergunta]
print(f"Você digitou o número {palavra}.")
