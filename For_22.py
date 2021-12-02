while True:
    N = int(input('Enter N: '))
    x = int(input('Enter x: '))

    ml = 1
    n_m = 1
    n_x = 1

    for i in range (1,N+1):
        ml = ml*1/i
        print (ml)
        n_m = n_m + (x**i)*ml
    print (n_m)
