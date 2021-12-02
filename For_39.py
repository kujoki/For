A = int (input('Enter A: '))
B = int (input('Enter B: '))

AB = B - A
i = -1
for _ in range (AB):
    i+=1
    x = A + i
    for s in range (x):
        print (x,end='')
    print (' ')
        
