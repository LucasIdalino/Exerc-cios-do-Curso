def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro! Por favor, digite um número inteiro.\033[m")
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return a


def linha(lin=42):
    return "=" * lin


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mEscolha sua Opção: \033[m')
    return opc
