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

from salvartxt import *

#--- Lista de passageiros que estão no terminal, e lista de avião vazia, pronta para receber os passageiros.
terminal = ['Presidiário','Policial' , 'Piloto', 'Oficial1', 'Oficial2', 'Chefe', 'Comissária1','Comissária2']
aviao = []

#--- Logica;/Função para mostrar/retornar a logistica de como os passageiros vão embar no avião. 
def transporte():                

    if not terminal:
        return ('Todos os passageiros já embarcaram! ')            
    elif terminal[0] == 'Presidiário' or terminal[0] == 'Policial':
        return (f'O {terminal[0]} está sendo transportado pelo {terminal[1]}')
    elif terminal[0] == 'Chefe' and terminal[1] != 'Piloto':
        return(f'O {terminal[1]} está sendo transportado pelo Chefe')
    elif terminal[0] == 'Chefe':
        return(f'O {terminal[0]} está sendo transportado pelo {terminal[1]}')
    elif terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto':
        return(f'A {terminal[1]} está sendo transportado pelo {terminal[0]}')

#--- Função que mostra o menu, onde as informações serão atualizadas a cada ENTER        
def menu():
    print (f'''
                ###############################################################
                
                Passageiros para Embarque: {terminal}
                {transporte()}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################\n''')

menu()

#--- Logica/Função que recebe como parâmetro as listas, a ao remover acada item de uma vai adicionando a outra,onde também são
#  aplicadas as condições/regras de transporte. A dinâmica muda quando ficam apenas dois elementos na lista, neste caso os dois
#  são removidas do terminal e addicionados ao avião. 
def mostrar(terminal,aviao):
    try: 
        while terminal.count != 0:
            a = input(f'\n Precione ENTER para continuar')
            
            if a == '':
                if terminal[0] == 'Chefe' and terminal[len(terminal)-1] != 'Chefe' and terminal[1]== 'Comissária2':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    pas = terminal.pop(0)
                    aviao.append(pas)
                    menu()

                elif terminal[0] == 'Chefe' and terminal[len(terminal)-1] != 'Chefe':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    menu()    

                elif terminal[0] == 'Piloto' and terminal[1] != 'Chefe':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    menu()

                else:
                    pas = terminal.pop(0)
                    aviao.append(pas)
                    menu()
    except IndexError:
        print('Todos estão no avião.')

mostrar(terminal,aviao)
txt_terminal(embarque)
txt_aviao(aviao)