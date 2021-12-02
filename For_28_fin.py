while True:
    x = float(input('Enter: '))
    n = int(input('Enter n: '))

    s = 1 + x/2
    b = 0
    a = -1
    ap = 1
    bp = 1
    sign = 1

    for _ in range(n-1):
        b+=2
        a+=2
        bp*=b
        ap*=a
        sign*=(-1)
        s+=sign*ap*x**(b)/(bp*(b+2))
    print(s)
