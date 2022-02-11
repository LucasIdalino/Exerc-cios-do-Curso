from Pythonexercicios.ex111.UtilidadesCeV import moeda


p = float(input('Digite um valor: '))
moeda.resumo(p, taxa=int(input('Aumento: ')),
             taxar=int(input('Redução: ')))
