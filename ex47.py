cont = soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont +=1
    soma +=num
print(f'Voce digitou {cont} numeros e a soma deles é {soma}')