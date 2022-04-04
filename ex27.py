n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if media >= 7:
    print('Sua nota {} esta aprovada!!!'.format(media))
elif media < 5:
    print('Sua nota é: {} e voce esta reprovado!!!!'.format(media))
else:
    print('Sua nota é: {} e voce esta na recuperação!'.format(media))