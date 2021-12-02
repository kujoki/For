while True:
    N = int(input('Enter N: '))
    A = int(input('Enter A: '))

    m = 1
    for _ in range(N):
        m*=A
    print (m)
