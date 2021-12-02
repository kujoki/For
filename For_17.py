while True:
    N = int(input('Enter N: '))
    A = int(input('Enter A: '))
    sm = 1

    for i in range(1,N):
        F = A**i
        sm = sm + F
    print(F)
