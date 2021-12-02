while True:
    N = int(input('Enter: '))

    a = -1
    s = 0
    for _ in range(N):
        a+=2
        s+=a
    print (s)
