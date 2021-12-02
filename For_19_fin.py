while True:
    N = int(input('Enter: '))
    s = 1
    b = 0
    for _ in range(N):
        b+=1
        s*=b
    print (s)
