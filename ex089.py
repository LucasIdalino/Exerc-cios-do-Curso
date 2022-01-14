ficha = list()
while True:
    nome = str(input("Aluno: ")).upper()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    pergunta = str(input("Quer cadastrar mais? [S/N] ")).upper()[0]
    if "N" in pergunta:
        break
print("*="*20)
print(f'{"no":<4}{"Nome":<10}{"media":>8}')
for p, v in enumerate(ficha):
    print(f"{p:<4}{v[0]:<10}{v[2]:>8}")
while True:
    print("*="*20)
    opc = int(input("Escolha qual aluno você quer ver as notas: "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"Aqui estão as notas do aluno(a) {ficha[opc][0]}: {ficha[opc][1]}.")
    if opc > len(ficha) - 1:
        print("Aluno não encontrado. Tente novamente.")
print(ficha)
