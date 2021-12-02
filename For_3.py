while True:
    A = int(input('A: '))
    B = int(input('B: '))
    
    '''
    k = []
    N = abs(B - A)
    B = B - 1
    for i in range(N - 1):
        k.append(B-i)
    print ('Общее число:', N - 1)
    print (k)
    '''
    '''
    k = []
    N = abs(B - A)
    for i in range(1,N):
        k.append(B-i)
    print ('Общее число:', N-1)
    print (k)
    '''
    for i in range(B-1, A, -1):
        print(i, end=' ')
    print()
    print(B-A-1)
