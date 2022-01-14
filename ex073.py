times = ("Atlético - MG", "Palmeiras", "Flamengo", "Bragatino", "Fortaleza",
         "Corinthians", "Internacional", "Fluminense", "Cuiabá", "Ceará - SC",
         "Athletico - PR", "América - MG", "Atlético - GO", "São Paulo",
         "Bahia", "Santos", "Sport Recife", "Juventude", "Grêmio", "Chapecoense")

print(("="*20), "Brasileirão - Série A", ("="*20))
print("="*10)
print("Os Primeiros 5 colocados:", times[0:5])
print("="*10)
print("Os últimos 4 colocados:", times[16:21])
print("="*10)

#A função sorted(), organiza os valores da tupla em ordem alfabética.
print("Times em ordem alfabética:", sorted(times))
print("="*10)
#A função index() identifica a posição do valor ou string passado como parâmetro. 
print(f"O time da Chapecoense está na {times.index('Chapecoense')+1}ª posição.")
