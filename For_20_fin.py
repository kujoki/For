while True:
    N = int(input('Enter: '))


    a = 0
    b = 1
    s = 0
    for _ in range(N):
        a+=1
        b*=a
        s+=b
    print (s)
