velocidade_do_carro = int(input("Quantos km/h seu carro está? "))
if velocidade_do_carro > 80:
    print("Você foi multado! Você excedeu o limite de km/h permitido que é de 80km/h.")
    multa = (velocidade_do_carro - 80)*7
    print("Você pagará uma multa de {:.2f}R$ pelo limite de velocidade excedido.".format(multa))
print("Boa noite. Dirija com segurança!")
