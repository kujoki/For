while True:
    N = int(input('Enter: '))

    a = 0
    s = 0
    b = 200 #who cares
    for i in range (N):
        a = a + 1
        b = 1/a
        s+=b
    print (s)
