while True:
    x = float(input('Enter: '))
    N = int(input('Enter: '))

    a = 0
    k = 0
    b = 1
    s = 1

    for _ in range(N):
        a+=1 #недосчетчик
        b*=a #факториал
        k = x**a #степень
        s+=k/b
    print (s)
