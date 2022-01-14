from datetime import datetime
dados = {}
dados["Nome"] = str(input("Nome: ").upper())
data = int(input("Ano de Nascimento: "))
dados["Idade"] = datetime.now().year - data
dados["CTPS"] = int(input("CTPS (Digite 0 se não tiver Carteira de Trabalho): "))
if dados["CTPS"] != 0:
    dados["Ano de Contratação"] = int(input("Ano de Contratação: "))
    dados["Salário"] = int(input("Salário atual: "))
    dados["Ano de Aposentadoria"] = (dados["Idade"] + (dados["Ano de Contratação"] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f"{k} tem o valor de {v}...")
