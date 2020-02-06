#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

nome = input('Insita o nome do funcionário: ')
sobrenome = input('Insita o sobrenome do funcionário: ')
cpf = input('Insita o CPF do funcionário: ')
rg = input('Insita o RG do funcionário: ')
salario = round(float(input('Insita o salário do funcionário: ')),2)

print('\nNome: {}\nSobrenome: {}\nCPF: {}\nRG: {}\nSalário: {}\n'.format(nome,sobrenome,cpf,rg,salario))
