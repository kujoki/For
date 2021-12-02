import math
while True:
    A = float(input('Enter A: '))
    B = float(input('Enter B: '))
    N = int(input('Enter N: '))



    AB = abs(A-B)
    H_ab = AB/N
    k = -1
    for _ in range(N+1):
        k+=1
        x = A + H_ab*k
        print ('Координата: ',x)
        f = 1 + math.sin(x)
        print('Синус: ',f)
    print ('Длина отрезка: ',H_ab)
