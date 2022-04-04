velo = int(input('Em que velocidade seu carro estava?'))
if velo > 80:
    multa = (velo - 80) * 7
    print("MULTADO! Voce ultrapassou o limite de velocidade!")
    print("Sua multa é de {:.2f}RS".format(multa))
else:
    print("Seu limite de velocidade esta correto! Tenha um bom dia!")