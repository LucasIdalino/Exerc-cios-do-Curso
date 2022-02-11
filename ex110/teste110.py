from Pythonexercicios.ex110 import moeda

n = float(input("Digite um valor: R$ "))
(moeda.resumo(n, taxa=int(input("Aumento: ")),
              taxar=int(input('Redução: '))))
