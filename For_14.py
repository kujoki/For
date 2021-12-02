import numpy as np
N = int(input('Enter: '))

ml = 0
for i in np.arange(1, 2*N+1, 2):
    k = i
    ml = ml+k
    print (k)

print ('Квадрат введеного числа: ',ml)
