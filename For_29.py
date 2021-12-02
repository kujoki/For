while True:
    A = float(input('Enter A: '))
    B = float(input('Enter B: '))
    N = int(input('Enter N: '))


    AB = abs(B-A)
    H_ab = AB/N
    k = -1
    for _ in range(N+1):
        k+=1
        s = A + H_ab*(k)
        print ('Точка: ', s)
    print ('Длина отрезка: ',H_ab)







    
