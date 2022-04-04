dist=float(input('Sua viagem é de quantos km?'))
if dist <=200:
    valor= dist * 0.50
else:
    valor = dist * 0.45
print('O valor total sera de {:.2f} reais'.format(valor))