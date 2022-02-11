from Pythonexercicios.ex108 import moeda

n = float(input('Digite um valor R$ '))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O aumento de 10% de {moeda.moeda(n)} é {moeda.moeda(moeda.aumento(n, 10))}')
print(f'A diminuição de 10% de {moeda.moeda(n)} é {moeda.moeda(moeda.diminuir(n, 10))}')
