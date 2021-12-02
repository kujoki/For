import numpy as np
N = int(input('Enter: '))

ml = 1
for i in np.arange(1, N+1, 1):
    k = i*0.1+1
    ml = ml*k
    print (k)

print (ml)
