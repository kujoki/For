while True:
    K = int(input('Enter: '))

    a = 1
    b = 2
    c = 3
    for _ in range (K):
        d = c + b - 2*a
        a = b
        b = c
        c = d
        print (d)
