while True:
    A = int(input('A: '))
    B = int(input('B: '))
    N = abs(B-A)
    mltpl = A*A

    for i in range (1,N+1):
        k = A + i
        mltpl = mltpl + k**2
    print (mltpl)
