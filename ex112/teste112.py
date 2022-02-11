from Pythonexercicios.ex111.UtilidadesCeV import moeda
from Pythonexercicios.ex112.UtilidadesCeV import dados


p = dados.leiadinheiro("Digite um valor R$ ")
moeda.resumo(p, taxa=int(input('Aumento: ')),
             taxar=int(input('Redução: ')))
