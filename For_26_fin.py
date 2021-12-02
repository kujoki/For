while True:
    x = float(input('Enter: '))
    n = int(input('Enter n: '))


    f = -1
    sign = -1
    s = 0
    k = 1
    for _ in range(n+1):
        f+=2
        sign*=(-1)
        s+=sign*(x**f)/f
        print(s)
    print ('fin:',s)
