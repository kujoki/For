while True:
    K = int(input('Enter: '))

    a = 1
    b = 2
    for _ in range(K):
        c = (b + 2*a)/3
        a = b
        b = c
        print (c)
        
