# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

embarque = []
terminial = []
aviao = []
passageiros = ['Piloto','Oficial1','Oficial2','ChefeDeServico','Comissaria1','Comissaria2']

piloto = 7
while piloto <1 or piloto >6:
    piloto = int(input('Informe o motorista: \n1- Piloto\n2- Oficial1\n3- Oficial2\n4- Chefe de Serviço\n5- Comissaria1\n6- Comissaria2\n'))
if piloto <1 or piloto >6:
    print('Opção Inválida')

passageiro = 7
while passageiro <1 or passageiro >6:
    passageiro = int(input('Informe o passageiro: \n1- Piloto\n2- Oficial1\n3- Oficial2\n4- Chefe de Serviço\n5- Comissaria1\n6- Comissaria2\n')
if passageiro <1 or passageiro >6:
    print('Opção Inválida')

saida = 9
chegada = 8

while saida > chegada:
    saida = input(float('Informe a saída: '))
    chegada = input(float('Informe a chegada: '))
    if saida > chegada:
        print('Horários Inválidos')

chegasai = {'saida':saida,'chegada':chegada}