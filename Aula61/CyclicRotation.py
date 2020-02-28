A = [1,2,3,4,5,6,7]
K = int(input('Quantas rotações você deseja fazer?: '))
print(f'Lista inicial: {A}')

def solution(K,A):
    for i in range(K):
        A.insert(0, A[-1])
        del(A[-1])
    print(f'Lista final: {A}')
    return A

solution(K,A)