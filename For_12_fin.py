while True:

    N = int(input('Enter: '))
    
    a = 0 #важно
    b = 0 #неважно
    s = 0 #важно
    for _ in range(N):
        a+=1
        b = a/10 + 1
        s+=b
    print (s)
