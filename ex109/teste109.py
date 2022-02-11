from Pythonexercicios.ex109 import moeda

n = float(input("Digite um valor: R$ "))

print(f"O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}")
print(f"A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}")
print(f'O valor com 10% de aumento fica {moeda.aumento(n, 10, True)}')
print(f'O valor com 13% de diminuição fica {moeda.diminuir(n, 13, True)}')
