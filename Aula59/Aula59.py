#---- Métodos
#---- Argumentos Ordenados
#---- Argumentos Nomeados

def soma(n1,n2):
    resultado = n1+n2
    return  resultado

res = soma(10,20)
print(res)

def multiplicacao(n1,n2,n3):
    resultado = n1 * n2 * n3
    return  resultado

res = multiplicacao(10,20,30)
print(res)

def subtracao(n1,n2,n3):
    resultado = n1-n2-n3
    return resultado

res2 - subtracao(n1=10,n2=20,n3=10)
print(res2)

def multiplicacao(n1,n2=1,n3=1):
    return n1*n2*n3

res3 = multiplicacao(n1,n2,n3)
print(res3)