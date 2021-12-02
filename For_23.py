while True:
    N = int(input('Enter N: '))
    x = int(input('Enter x: '))

    ml = 1
    n_m = 0

    for i in range (1,2*N+1,1):
        ml = ml*1/(2*i+1)
        n_m = n_m + (x**(2*i+1))*ml*(-1)**(i)
        print (n_m)
    print (n_m)
