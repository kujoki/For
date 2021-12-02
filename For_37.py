while True:
    N = int(input('E: '))
    s = 0
    k = 0
    for i in range(N):
        k+=1
        s+=k**k
        print (s)
