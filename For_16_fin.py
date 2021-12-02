
while True:
    A = float(input('Enter A: '))
    N = int(input('Enter N: '))

    s = 1
    for _ in range(N):
        s*=A
        print (s)
