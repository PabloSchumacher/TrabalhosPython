terminal = ['Presidiário','Policial' , 'Chefe', 'Oficial1', 'Oficial2','Piloto', 'Comissária1','Comissária2']
aviao = []

def transporte():
    if not terminal:
        return(f'Todos foram transportados')
    elif terminal[0] == 'Presidiário' or terminal[0] == 'Policial':
        return(f'O {terminal[0]} está sendo transportado e o {terminal[1]} está dirigindo.')
    elif terminal[0] == 'Chefe' and terminal[1] != 'Piloto':
        return(f'O {terminal[1]} está sendo transportado e o {terminal[0]} está dirigindo.')
    elif terminal[0] == 'Chefe':
        return(f'O {terminal[0]} está sendo transportado e o {terminal[1]} está dirigindo.')
    elif terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto.':
        return(f'A {terminal[1]} está sendo transportado e o {terminal[0]} está dirigindo.')


def menu():
    print (f'''
                ###############################################################
                
                Passageiros para Embarque: {terminal}
                {transporte()}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################\n''')
                

menu()

def mostrar(terminal,aviao):
    try: 
        while terminal.count != 0:
            a = input('\nPrecione ENTER para continuar')
            
            if a == '':

                if terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto' and terminal[1] == 'Comissária2':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    pas = terminal.pop(0)
                    aviao.append(pas)

                    menu()
                    
                elif terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto':
                    pas = terminal.pop(1)
                    aviao.append(pas)

                    menu()

                elif terminal[0] == 'Chefe' and terminal[1] != 'Piloto':
                    pas = terminal.pop(1)
                    aviao.append(pas)

                    menu()

                else:
                    pas = terminal.pop(0)
                    aviao.append(pas)

                    menu()
    except IndexError as erro:
        print('Erro de retirar um elemento que não existe: ', erro)
        print('Todos estão no avião.')

mostrar(terminal,aviao)