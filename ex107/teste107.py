from Pythonexercicios.ex107 import moeda

n = int(input("Digite um valor: R$ "))
print(f"O dobro de R${n} é R${moeda.dobro(n):.2f}")
print(f"A metade de R${n} é R${moeda.metade(n):.2f}")
print(f'O valor R${n} com 10% de aumento fica R${moeda.aumentar(n, 10):.2f}')
print(f'O valor R${n} com 13% de diminuição fica R${moeda.diminuir(n, 13):.2f}')
