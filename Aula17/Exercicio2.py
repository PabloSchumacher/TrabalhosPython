from random  import randint
aleatorio = randint(1,100)

n=0
while n != aleatorio :
    n = int(input('Informe o número: '))
    if n == aleatorio:
        print('Você acertou')
        # break
    else:
        print('Você errou')
        if n > aleatorio:
            print(f'O número informado ({n}) é maior!')
        else:
            print(f'O número informado ({n}) é menor!')