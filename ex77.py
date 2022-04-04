from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print('Não pode votar')
    elif 16<= idade < 18 or idade > 65:
        print('Voto opicional')
    else:
        print('Voto Obrigatorio')

voto(1920)