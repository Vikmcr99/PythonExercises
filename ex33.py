s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 ==0:
        s +=num
        cont += 1
print('existem {} numeros pares e a soma deles é: {}'. format(cont,s))
