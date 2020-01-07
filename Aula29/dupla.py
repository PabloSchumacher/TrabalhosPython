terminal = ['Presidiário','Policial' , 'Chefe', 'Oficial1', 'Oficial2','Piloto', 'Comissária1','Comissária2']
aviao = []
carro = []

def mostrar(terminal,aviao,carro):
    while terminal.count != 0:
        a = input('Precione ENTER para continuar')
        
        if a == '':
            if terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto':
                pas = terminal.pop(1)
                aviao.append(pas)

                print (f'''
                ###############################################################

                Passageiros para Embarque: {terminal}  
                Passageiros no Carro: {carro}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################''')

            elif terminal[0] == 'Chefe' and terminal[1] != 'Piloto':
                pas = terminal.pop(1)
                aviao.append(pas)

                print (f'''
                ###############################################################

                Passageiros para Embarque: {terminal}  
                Passageiros no Carro: {carro}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################''')

            else:
                pas = terminal.pop(0)
                aviao.append(pas)

                print (f'''
                ###############################################################

                Passageiros para Embarque: {terminal}  
                Passageiros no Carro: {carro}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################''')
    
mostrar(terminal,aviao,carro)