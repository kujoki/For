while True:
    N = int(input('Enter: '))
    b = 0 #who cares
    s = 0 #важно
    a = N-1 #нулевой элемент последовательности
    for _ in range(N+1):
        a = a + 1
        b = a**2
        s= s + b
    print (s)
