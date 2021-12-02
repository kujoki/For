while True:
    A = int(input('Enter A: '))
    N = int(input('Enter N: '))
    k = []

    for i in range (1,N+1):
        k.append(A**i)
    print(k)
