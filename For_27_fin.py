while True:
    x = float(input('Enter: '))
    n = int(input('Enter n: '))


    a = -1
    b = 0
    s = x
    ap = 1
    bp = 1
    for _ in range(n-1):
        a+=2
        b+=2
        ap*=a
        bp*=b
        s+=ap*x**(b+1)/(bp*(b+1))
        print (s)
