while True:
    N = int(input('Enter N: '))
    A = int(input('Enter A: '))
    F = A

    for i in range(N-1):
        F = F*A
    print(F)
