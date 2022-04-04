dias=int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram percorridos?'))
pagar = (dias * 60) + 0.15 * km
print("O valor total a pagar é de {:.2f} reais!".format(pagar))