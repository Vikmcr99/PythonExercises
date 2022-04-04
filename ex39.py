sexo = str(input('Sexo masculino ou feminino? [M/F]:')).upper()
while sexo not in 'MF':
    sexo=str(input('Ops, tente novamente:')).upper()
print('Sexo {} registrado com sucesso!'.format(sexo))