sal = float(input('Digite seu salario para calcularmos o reajuste:'))
if sal > 1250:
    novosal = (sal * 0.10) + sal
else:
    novosal = (sal * 0.15) + sal

print('O seu novo salario é: {:.2f} reais'.format(novosal))