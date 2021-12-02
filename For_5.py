import numpy as np
n = float(input('Enter: '))
c = []

for i in np.arange(0.1, 1.1, 0.1):
    c = n*i
    print (c)

for i in range(1, 11):
    print(n*i*0.1)
