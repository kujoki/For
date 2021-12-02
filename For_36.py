while True:
    k = int(input('Enter k: '))
    N = int(input('Enter N: '))
    a = 0
    s = 0
    for _ in range(N):
        a+=1
        b = a**k
        s+=b
    print (s)
