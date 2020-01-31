#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido

nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
n = input('Digite o número do registro: ')
cargo = input('Digite o seu cargo: ')
salario = float(input('Digite seu salário: '))

if salario <= 1751.81:
    print(f'Seu salário liquido é: {salario*0.92}')
elif salario >= 1751.82 and salario <= 2919.72:
    if salario >= 1903.98 and salario <= 2826.65:
        print(f'Seu salário liquido é: {salario*0.83}')
    elif salario >= 2826.66 and salario <= 2919.72:
        print(f'Seu salário liquido é: {salario*0.755}')
    else:
        print(f'Seu salário liquido é: {salario*0.905}')

elif salario >= 2919.72 and salario <= 3751.05:
    print(f'Seu salário liquido é: {salario*0.74}')
elif salario >= 3751.06 and salario <= 4664.68:
    print(f'Seu salário liquido é: {salario*0.665}')
else:
    print(f'Seu salário liquido é: {salario*0.725}')