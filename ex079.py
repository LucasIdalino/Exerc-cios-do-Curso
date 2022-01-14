lista = list()
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:

        #O método .append() adiciona um valor no final de uma lista quando posto no parâmetro
        lista.append(n)
        print(f"O número foi adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:

                #O método .insert(), inseri um valor em uma posição da lista.
                lista.insert(pos, n)
                print(f"Número adicionado na posição {pos} da lista")
                break
        pos += 1
print("*="*30)
print(f"Os valores digitados em ordem foram {lista}.")
