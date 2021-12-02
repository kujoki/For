while True:
    A = float(input('Enter A: '))
    N = int(input('Enter N: '))

    s = 0 #важно
    b = 0 # неважно
    a = -1 #важно
    for _ in range(N+1):
        a+=1
        b = A**a
        s+=b
    print(s)
