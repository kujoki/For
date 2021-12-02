while True:
    x = float(input('Enter: '))
    n = int(input('Enter n: '))

    s = 1 # важно
    sign = 1
    b = -1
    c = 0
    f = 1
    for _ in range(n-1):
        b+=2
        c+=2
        f*=b*c 
        sign*=(-1)
        k = (x**c)*sign
        s+=k/f
    print (s)
    
