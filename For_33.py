while True:
    N = int(input('Enter: '))

    a = 1
    b = 1
    for _ in range(N):
        c = a+b
        a = b
        b = c
        print (c,'', end = '')
    print ('')
