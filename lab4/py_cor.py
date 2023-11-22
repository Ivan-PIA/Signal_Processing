import matplotlib.pyplot as plt
import numpy as np



def autocorrelate(a,b,size):
    c = 0
    o = 0
    for i in range(size):
        if a[i] == b[i]:
            c+=1
        else:
            o+=1
    return c - o

def print_table(a,size):
    for i in range(size):
        print(f"|  {a[i]}  ", end='')

def preampula():
    for i in range(31):
        print("| b%2d "%(i), end='')
    print("| Autocorrelate|")


x = [0,1,1,1,1] 
y = [1,0,1,1,0]
x1 = [1,0,0,0,0] 
y1 = [1,0,0,0,1]
last_x = []
last_y = []
last_x1 = []
last_y1 = []
psevdo = []
autocor = []
new_psevdo = []
size = 31

for i in range(size):
    #print(x)
    last_x.append(x[4])
    temp_x = x[2] ^ x[3]
    x = x[-1:] + x[:-1]
    x[0] = temp_x
    
    last_y.append(y[4])
    temp_y = y[1] ^ y[2]
    y = y[-1:] + y[:-1]
    y[0] = temp_y



for i in range(size):   
    psevdo.append(last_x[i] ^ last_y[i])
# -----------------------------------------------
for i in range(size): #x1 y1
    #print(x)
    last_x1.append(x1[4])
    temp_x = x1[2] ^ x1[3]
    x1 = x1[-1:] + x1[:-1]
    x1[0] = temp_x
    
    last_y1.append(y1[4])
    temp_y = y1[1] ^ y1[2]
    y1 = y1[-1:] + y1[:-1]
    y1[0] = temp_y

for i in range(size):   
    new_psevdo.append(last_x1[i] ^ last_y1[i])

print(new_psevdo)
preampula()

orig_psevdo = psevdo
print_table(psevdo,size)
cor = autocorrelate(psevdo, orig_psevdo, size)

print("|  %2d/31       |" % (cor))

for i in range(size):  
    psevdo = psevdo[-1:] + psevdo[:-1]
    print_table(psevdo,size)
    cor = autocorrelate(psevdo, orig_psevdo, size)
    autocor.append(cor/size)
    print("|  %2d/31       |" % (cor))


print("Исходная последовательность: ", psevdo)
print("Новая последовательность:    ", new_psevdo)
a = np.asarray(psevdo)
b = np.asarray(new_psevdo)
corelat = np.correlate(a,b)
print("Значение взаимной корреляции исходной и новой последовательностей : " ,corelat );

lag =np.arange(size)

plt.plot(lag,autocor)
plt.show()

