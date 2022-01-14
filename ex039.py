from datetime import date
print("SAIBA SE VOCÊ PRECISA SE ALISTAR NO EXERCITO")

ano_nascimento = int(input("Que ano você nasceu? "))
idade = date.today().year - ano_nascimento
print("Você tem {} anos.". format(idade))
if idade < 18:
    ano = 18 - idade
    print("Você ainda vai se alistar.")
    print("Falta(m) {} ano(s) para você se alistar.".format(ano))
    print("Seu alistamento será no ano de {}.".format(ano + date.today().year))
elif idade == 18:
    print("Está na hora de se alistar.")
elif idade > 18:
    ano = idade - 18
    print("Já passou da hora de se alistar.")
    print("Já se passaram {} ano(s) do prazo para o alistamento.".format(ano))
    print("O ano de alistamento foi em {}.".format(date.today().year - ano))
