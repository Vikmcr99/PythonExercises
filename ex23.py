valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual é o seu salario?'))
anos=int(input('Em quantos anos voce vai pagar?'))
prest= valor/(anos*12)
if salario * 0.30 < prest:
    print("NEGADO! o emprestimo nao pode ser feito")
else:
    print("Emprestimo aprovado! a prestaçao mensal sera de: {:.2f} reais".format(prest))