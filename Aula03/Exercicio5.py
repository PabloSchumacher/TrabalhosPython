#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria
#--- Deve ser utilizado a função format e os caracteres de tabulação e quebra de linha para cada categoria

salario = float(input('Informe seu salário: '))
print(f'Destinado a despesas fixas: R${salario*0.5}')
print(f'Destinado a investimentos de longo prazo como aposentadoria e independência financeira: R${salario*0.20}')
print(f'Destinado a investimentos de curto prazo, podendo ser uma reserva de emergência, uma viagem, um carro, etc: R${salario*0.10}')
print(f'Para gastos livres e despesas variáveis: R${salario*0.20}')