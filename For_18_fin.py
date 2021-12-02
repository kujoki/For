while True:
    A = float(input('Введите число A: '))
    N = int(input('введите число N: '))

    b = 0 # неважно
    s = 0
    a = -1 
    for _ in range(N+1):
        a+=1
        b = (A**a)*(-1)**(a)
        s+=b
    print (s)
