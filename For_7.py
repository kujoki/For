while True:
    A = int(input('A: '))
    B = int(input('B: '))
    N = abs(B-A)
    sum = A

    for i in range (1,N+1):
        k = A + i
        sum = sum + k
    print (sum)
