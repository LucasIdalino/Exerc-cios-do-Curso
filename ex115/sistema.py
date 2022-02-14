from Pythonexercicios.ex115.lib.interface import *
from Pythonexercicios.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:

    opc = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if opc == 1:
        # Opção de listar conteúdo de um arquivo.
        lerarquivo(arq)
    elif opc == 2:
        # Opção de Cadastrar Uma Nova Pessoa.
        cabecalho('Cadastrar Uma Nova Pessoa')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        escreverarquivo(arq, nome, idade)
    elif opc == 3:
        # Opção de Sair do Sistema.
        cabecalho('Saindo do programa. Muito Obrigado.')
        break
    else:
        print('Erro! Opção inválida.')
    sleep(1)

