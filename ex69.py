from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if dados['ctps'] == 0:
    print('-' * 40)
    for k, v in dados.items():
        print(f'{k} = {v}')
else:
    dados['contratacao'] = int(input('Ano da contratação: '))
    dados ['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - nasc
    for k, v in dados.items():
        print(f'{k} = {v}')