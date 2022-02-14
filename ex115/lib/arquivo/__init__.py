from Pythonexercicios.ex115.lib.interface import *


def arquivoexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Não foi possível criar o arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Não foi possível ler o arquivo.')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def escreverarquivo(arq, nome='desconhecido', idade='0'):
    try:
        a = open(arq, 'at')
    except:
        print('Não foi possível abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Não foi possível escrever dados no arquivo.')
        else:
            print(f'Novo registro de {nome} foi adicionado.')
            a.close()



