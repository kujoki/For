while True:
    x = float(input('Enter x: '))
    n = int(input('Enter n: '))

    s = x
    c = 1
    sign = 1
    b = 0
    f = 1
    
    for _ in range(n):
        b+=2
        c+=2
        f*=b*c 
        sign*=(-1)
        k = (x**c)*sign
        s+=k/f
    print (s)
                                                                        
