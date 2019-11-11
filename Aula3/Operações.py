nome = input('Digite seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite sua idade: '))

print(f'Seu nome é {nome} {sobrenome} e você tem {idade} anos')

if idade < 18:
    print('Não pode usar o mercado Tech, para o que presta')
else:
    print('Pode usar mercado Tech e chapar o coco')
