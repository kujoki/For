while True:
    N = int(input('Enter: '))

    ml = 1
    n_m = 0

    for i in range (1,N+1):
        ml = ml*1/i
        print (ml)
        n_m = n_m + ml
    print (n_m)
