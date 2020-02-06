#--- Exercicio 5  - Variávies e impressão com interpolacão de string
#--- Imprima os dados de 5 papeis cotatos na bolsa de valors de SP
#--- Os dados dos papeis devem estar em variáveis
#--- Papel: Nome, Tipo, Cotação Atual e Valores Min e Max do dia 
#--- A tela deve conter cabeçalho e rodapé 

nome1 = 'Petrobras (PETR4)'
nome2 = 'Copel (CPLE6)'
nome3 = 'Lojas Marisa (AMAR3)'
nome4 = 'JBS (JBSS3)'
nome5 = 'Pine (PINE4)'
tipo1 = 'Petróleo'
tipo2 = 'Utilities'
tipo3 = 'Varejo de moda'
tipo4 = 'Carnes'
tipo5 = 'Financeiro'
cotação1 = 29.30
cotação2 = 58.90
cotação3 = 10.09
cotação4 = 26.23
cotação5 = 3.19
valmax1 = 30.10
valmax2 = 59.56
valmax3 = 10.09
valmax4 = 27.64
valmax5 = 3.26
valmin1 = 29.27
valmin2 = 58.41
valmin3 = 10.09
valmin4 = 26.10
valmin5 = 3.15

print('\nPapeis: \n')
print(f'Nome:{nome1}, Tipo:{tipo1}, Cotação:{cotação1}, Valor Máximo do dia:{valmax1}, Valor Mínimo do dia:{valmin1}')
print(f'Nome:{nome2}, Tipo:{tipo2}, Cotação:{cotação2}, Valor Máximo do dia:{valmax2}, Valor Mínimo do dia:{valmin2}')
print(f'Nome:{nome3}, Tipo:{tipo3}, Cotação:{cotação3}, Valor Máximo do dia:{valmax3}, Valor Mínimo do dia:{valmin3}')
print(f'Nome:{nome4}, Tipo:{tipo4}, Cotação:{cotação4}, Valor Máximo do dia:{valmax4}, Valor Mínimo do dia:{valmin4}')
print(f'Nome:{nome5}, Tipo:{tipo5}, Cotação:{cotação5}, Valor Máximo do dia:{valmax5}, Valor Mínimo do dia:{valmin5}\n')