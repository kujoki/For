while True:
    A = int(input('A: '))
    B = int(input('B: '))
    
    '''
    N = B - A
    for i in range(N+1):
        k = A+i
        print (k)
    print ('Общее число:', N + 1)
    '''
    '''
    k = []
    N = B - A

    for i in range(N+1):
        k.append(A+i)
    print ('Общее число:', N + 1)
    print (k)
    '''
    for i in range(A, B+1):
        print(i, end=' ')
    print()
    print(B-A+1)
