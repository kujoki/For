import numpy as np
N = int(input('Enter: '))

ml = N*N
for i in np.arange(1, N+1, 1):
    k = (N+i)**2
    ml = ml + k
    print (k)

print (ml)
