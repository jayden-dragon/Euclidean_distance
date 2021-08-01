import numpy as np

import csv

import re

import tensorflow as tf

import math

from tensorflow.keras.preprocessing import sequence

 

r = open('C:/Users/jayden/Desktop/2_bd_pnts.txt', mode='rt', encoding='utf-8')

f = open('C:/Users/jayden/Desktop/bd_2.csv', 'w', newline='\n')

 

wr = csv.writer(f, delimiter=',')

 

data = []

i=0

 

 

# Coordinate extraction 

while r:

    line = r.readline()

    

    if i%2 == 1:

        data.append(re.findall("-?\d+", line))

                        

    if not line: break

     

    i=i+1

 



# Zero padding

data = sequence.pad_sequences(data, padding='post')

np.array(data)

 

np.savetxt('C:/Users/jayden/Desktop/bd_2.csv', data, fmt='%2d', delimiter=',')

    

r.close()    

f.close()

 

 

c1 = np.loadtxt('C:/Users/jayden/Desktop/bd_1.csv', delimiter=',', dtype=np.int64)

c2 = np.loadtxt('C:/Users/jayden/Desktop/bd_2.csv', delimiter=',', dtype=np.int64)

 

# remove coordinates out of range & match cam #1 and #2

 

for i in range(0, len(c1)):

    for j in range(0, 6):

        if j%2==0:

            if c1[i][j]!=0 or c2[i][j]!=0:

                c1[i][j]=c1[i][j]+640

                c2[i][j]=-c2[i][j+1]+1350

        else:

            if c1[i][j]!=0 or c2[i][j]!=0:

                c2[i][j]=c2[i][j-1]-1250

                

 

np.savetxt('C:/Users/jayden/Desktop/c1.csv', c1, fmt='%2d', delimiter=',')

np.savetxt('C:/Users/jayden/Desktop/c2.csv', c2, fmt='%2d', delimiter=',')

                

print(c1)

print(c2)

 

 

c3=np.zeros((421,12))

 

 

 

# Euclidean distance

 

def e_d(x, y):

    result=[]

    for w in range(0,6,2):

        z = (x[0]-y[w])^2+(x[1]-y[w+1])^2

        tmp = z  

        result.append(tmp)

        

    if  min(result)==result[0]:

        return 0

    

    elif  min(result)==result[1]:

        return 1

    

    elif  min(result)==result[2]:

        return 2

 

    

for a in range(0,len(c1)):

    for b in range(0,6,2):

        x = [c1[a][b],c1[a][b+1]]

        y = c2[a][:]

        if ((599<c1[a][b]<1280 and 279<c1[a][b+1]<730)and(599<c2[a][b]<1280 and 279<c2[a][b+1]<730)):

            c3[a][b]=(x[0]+y[e_d(x,y)*2])/2

            c3[a][b+1]=(x[1]+y[e_d(x,y)*2+1])/2

        else:

            c3[a]=np.hstack([c1[a],c2[a]])

 

print(c3)

np.savetxt('C:/Users/jayden/Desktop/c3.csv', c3, fmt='%2d', delimiter=',')