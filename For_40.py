A = int(input('Enter: '))
B = int(input('Enter: '))
i = 0
b = -1
N = B - A
for _ in range(N):
    i+=1
    b+=1
    x = A + b
    for s in range(i):
        print (x,end='')
    print(' ')
        
        
