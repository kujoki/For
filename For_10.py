while True:
    N = int(input('Enter: '))
    
    sum = 0
    for i in range(1,N+1):
        k = 1/i
        sum = sum + k
        print (k)

    print (sum)
