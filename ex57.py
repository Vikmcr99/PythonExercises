palavras = ('panda','peixe','tigre','lobo','coruja','bolsonaro','lula')
for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
