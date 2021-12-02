while True:
    N = int(input('E: '))
    k = N+1
    s = 0
    x = 0
    for _ in range(N):
        k-=1
        x+=1
        s+=x**k
        print (s)
