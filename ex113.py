def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print(f'Erro! Por favor digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print(f'\nO usuário decidiu não digitar nada.')
            return f'valor {0}'
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (KeyboardInterrupt, ValueError):
            print(f'Digite um valor flutuante.')
            continue
        except KeyboardInterrupt:
            print(f'O usuário não digitou nada.')
            return f'O valor é {0}.'
        else:
            return n


i = leiaint("Digite um número inteiro: ")
print(f'O usuário digitou {i}.')

a = leiafloat('Digite um número flutuante: ')
print(f'O usuário digitou {a}.')
