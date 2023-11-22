import matplotlib.pyplot as plt
import numpy as np



def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    


x = [0,1,1,1,1] 
y = [1,0,1,1,0]
last_x = []
last_y = []
psevdo = []

for i in range(31):
    #print(x)
    last_x.append(x[4])
    temp_x = x[2] ^ x[3]
    x = x[-1:] + x[:-1]
    x[0] = temp_x
    
    last_y.append(y[4])
    temp_y = y[1] ^ y[2]
    y = y[-1:] + y[:-1]
    y[0] = temp_y

for i in range(31):   
    psevdo.append(last_x[i] ^ last_y[i])


print(psevdo)


