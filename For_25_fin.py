while True:
    x = float(input('Enter x: '))
    n = int(input('Enter n: '))

    f = 0
    sign = -1
    k = 1
    s = 0
    for _ in range(n):
        f+=1
        sign*=(-1)
        s+=sign*(x**f)/f
    print(s)
