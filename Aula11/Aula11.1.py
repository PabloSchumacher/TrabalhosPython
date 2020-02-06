# Aula 11 - 21-11-2019
# Prova

#--- 1- Crie um programa que calcule
#---    o imposto ISS de um serviço de desenvolvimento de software
#---    ulilizar metodos
#--- 2- Crie um programa que calcule
#---    a rentabilidade anual de um investimento
#---    baseando-se em sua rentabilidade mensal (jutos compostos)
#---    a rentabilidade deve ser representada em % e R$
#---    utilizar metodos
#--- 3- crie um programa para calculo de investimento
#---    Solicitar a quantidade de cotas do tesouro selic 
#---    (Considerar o valor do tesouro Selic Hoje 21/11/2019)
#---    Calcular o valor total ate o vencimento do título
#---    utilizar metodos
#--- 4- 
#---    utilizar metodos
#--- 5- 

from Metodos01 import *
valor = float(input('Qual é o valor do projeto: '))
viss = iss(valor)
print(f'O valor do ISS é: {viss}')
