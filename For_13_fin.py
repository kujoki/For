while True:
    N = int(input('Enter: '))

    s = 0 # важно
    a = 0 # важно
    b = 0 # неважно
    for _ in range(N):
        a+=1
        b = (a/10 + 1)*(-1)**(a+1)
        s+=b
    print(s)
